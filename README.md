shadow-useragent
==============

`shadow-useragent` gives you access to the most commonly used UserAgents on the Internet, safe from outdated data.

Behold, the power of UserAgent: 
```python3
>>> import shadow_useragent
>>> ua = shadow_useragent.ShadowUserAgent()
>>> ua.percent(0.05)
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
>>> ua.most_common
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
```

When you use our library, we register your User Agent, and update the frequency of use. The percent of use is thus dynamically updated, and never outdated. No more unused header that reveals your true identity, you are protected by the group.

Besides, you can rely on traditional features, like picking an header from outstanding IE browser family.


Feature Support
------------

`shadow-useragent` is the only safe, and updated user-agent package.

* UserAgent Percentage of Use
* Day-to-day Update
* Exhaustive UserAgents Family
* Elegant @property Methods
* Community-Based Package

`shadow-useragent` supports Python 2.7 & 3.4–3.7, and runs great on PyPy.

Installation
------------

To install `shadow-useragent`, simply use pipenv (or pip, of course):

```shell
$ pip install shadow-useragent
👻  
```

Never disappointed.

Documentation
-----
Documentation is not available for now. Unlimited delivery coming soon.


Usage
-----
```python3

import shadow_useragent 
ua = shadow_useragent.ShadowUserAgent()

# Access user-agent per Percentage of Use
ua = ua.percent(0.03) 
ua = ua.most_common

# Access user-agent per Browser Family
ua = ua.firefox 
ua = ua.chrome 
ua = ua.safari 
ua = ua.edge 
ua = ua.ie
ua = ua.android
ua = ua.ipad

# Random Access ;)
ua = ua.random
ua = ua.random_nomobile # Mobile-UA excluded

# If you want an Exhaustive list, you can play with
uas = ua.get_uas()
uas = ua.get_sorted_uas()  # Sorted List per Percentage of Use

>>> uas[0]
{
  'id':1,
  'scraping_time':'2019-07-31T17:05:15Z',
  'percent':9.6,
  'useragent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
  'system':'Chrome 75.0 Win10',
  'browser_family':'Chrome',
  'browser_version_string':'75.0.3770',
  'os_family':'Windows',
  'os_version_string':'10',
  'device_family':'Other',
  'device_brand':None,
  'device_model':None
}
```

Notes
-----
Contact for any issues or request : **simon.rochwerg@lobstr.io**

`shadow-useragent` stores collected UAs in the folder of your pip packages: site-packages/shadow_useragent/data.

The UserAgents' list is automatically updated with a shadow call (mm) to the shadow-useragent API every 24 hours. 
If you want to force the update :

```python3
from shadow_useragent import ShadowUserAgent
shadow_useragent = ShadowUserAgent()
shadow_useragent.force_update()
```
[![Run on Repl.it](https://repl.it/badge/github/lobstrio/shadow-useragent)](https://repl.it/github/lobstrio/shadow-useragent)