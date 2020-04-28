import requests
import pickle
from pytz import timezone
from datetime import datetime, timedelta
import logging, coloredlogs
import json
import random
import traceback
import os


class ShadowUserAgent(object):

    URL = "http://51.158.74.109/useragents/?format=json"
    path = os.path.join(
        (
            os.environ.get('LOCALAPPDATA') or
            os.environ.get('XDG_CACHE_HOME') or
            os.path.join(os.environ['HOME'], '.cache')
        ),
        __name__
    )
    useragents = os.path.join(path, 'useragents.pk')
    infos = os.path.join(path, 'infos.pk')

    def __init__(self, level="CRITICAL"):
        self.timezone = timezone('Europe/Paris')
        self.logger = logging.getLogger('shadow-useragent')
        formatter = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(lineno)d:%(funcName)s %(message)s'
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)
        coloredlogs.install(level=level, logger=self.logger, fmt=formatter)

    def _update(self):
        os.makedirs(self.path, exist_ok=True)
        d_infos = {}

        update_tries = 0
        while 1:
            try:
                update_tries += 1
                r = requests.get(url=self.URL)
                data = json.loads(r.content.decode('utf-8'))
            except Exception:
                self.logger.error(r.content.decode('utf-8'))
                self.logger.warning(traceback.format_exc())
            else:
                break
            finally:
                if update_tries > 5:
                    raise Exception("API Unavailable")
        with open(self.useragents, 'wb') as f:
            pickle.dump(data, f)
        d_infos["last_update"] = datetime.now(self.timezone)

        with open(self.infos, 'wb') as f:
            pickle.dump(d_infos, f)

    def update(self):
        limit = datetime.now(self.timezone) - timedelta(hours=24)
        try:
            d_infos = pickle.load(open(self.infos, 'rb'))
        except FileNotFoundError:
            d_infos = {
                "last_update":
                    datetime.fromtimestamp(0, self.timezone)
            }
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
        return random.choice(limited_uas)["useragent"]

    def random_details(self):
        self.update()
        uas = pickle.load(open(self.useragents, 'rb'))
        return random.choice(uas)

    def get_useragent(self, browser_family=None, percent=None):
        uas = self.get_uas()
        random.shuffle(uas)
        for ua in uas:
            if browser_family:
                if ua["browser_family"] ==  browser_family:
                    return ua["useragent"]
            if percent:
                if ua["percent"] > percent:
                    return ua["useragent"]

    def get_most_common(self):
        sorted_uas = self.get_sorted_uas()
        return sorted_uas[0]["useragent"]

    def percent(self, percent):
        assert isinstance(percent, float)
        return self.get_useragent(percent=percent)

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

    @property
    def most_common(self):
        return self.get_most_common()
