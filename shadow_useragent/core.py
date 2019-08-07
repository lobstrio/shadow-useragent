import requests
import pickle
from pytz import timezone
from datetime import datetime, timedelta
import logging, coloredlogs
import json
import random
import traceback
import os


class ShadowUserAgent():

    URL = "http://51.158.74.109/useragents/?format=json"
    path = os.path.dirname(os.path.realpath(__file__))
    useragents = '{}/data/useragents.pk'.format(path)
    infos = '{}/data/infos.pk'.format(path)

    def __init__(self, level="CRITICAL"):
        self.timezone = timezone('Europe/Paris')
        self.logger = logging.getLogger('shadow-useragent')
        formatter = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(lineno)d:%(funcName)s %(message)s'
        stream_handler = logging.StreamHandler()
        # stream_handler.setLevel(logging.CRITICAL)
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)
        coloredlogs.install(level=level, logger=self.logger, fmt=formatter)

    def _update(self):
        d_infos = {}

        update_tries = 0
        while 1:
            try:
                update_tries += 1
                r = requests.get(url=self.URL)
            except Exception:
                self.logger.warning(traceback.format_exc())
            else:
                break
            finally:
                if update_tries > 5:
                    raise Exception("API Unavailable")
        data = json.loads(r.content)
        with open(self.useragents, 'wb') as f:
            pickle.dump(data, f)
        d_infos["last_update"] = datetime.now(self.timezone)

        with open(self.infos, 'wb') as f:
            pickle.dump(d_infos, f)

    def update(self):
        limit = datetime.now(self.timezone) - timedelta(hours=24)
        d_infos = pickle.load(open(self.infos, 'rb'))
        self.logger.error(d_infos)
        last_update = d_infos["last_update"]
        if last_update < limit:
            self.logger.warning("Last update was {}, Updating...".format(last_update))
            self._update()
            self.logger.warning("Update Done")
        else:
            self.logger.warning("Last update is {}, please use force_update() to force refresh".format(last_update))

    def force_update(self):
        self._update()

    def display_uas(self):
        uas = self.get_sorted_uas()
        for ua in uas:
            self.logger.info(ua)

    def get_uas(self):
        self.update()
        return pickle.load(open(self.useragents, 'rb'))

    def get_sorted_uas(self):
        self.update()
        uas = pickle.load(open(self.useragents, 'rb'))
        return sorted(uas, key = lambda i: i['percent'],reverse=True)


    def pickrandom(self, exclude_mobile=False):
        self.update()
        uas = pickle.load(open(self.useragents, 'rb'))
        limited_uas = [ua for ua in uas if ua["browser_family"] != "Other"]
        if exclude_mobile:
            limited_uas = [ua for ua in uas if ua["browser_family"] != "Android" and ua["browser_family"] != "Mobile Safari"]
        return random.choice(uas)["useragent"]

    def random_details(self):
        self.update()
        uas = pickle.load(open(self.useragents, 'rb'))
        return random.choice(uas)

    def get_useragent(self, browser_family):
        uas = self.get_sorted_uas()
        for ua in uas:
            if ua["browser_family"] == browser_family:
                return ua["useragent"]
    @property
    def random(self):
        return self.pickrandom()

    @property
    def random_nomobile(self):
        return self.pickrandom(exclude_mobile=True)

    @property
    def firefox(self):
        return self.get_useragent("Firefox")

    @property
    def chrome(self):
        return self.get_useragent("Chrome")

    @property
    def safari(self):
        return self.get_useragent("Safari")

    @property
    def edge(self):
        return self.get_useragent("Edge")

    @property
    def ie(self):
        return self.get_useragent("IE")

    @property
    def opera(self):
        return self.get_useragent("Opera")

    @property
    def android(self):
        return self.get_useragent("Android")

    @property
    def ipad(self):
        return self.get_useragent("Mobile Safari")
