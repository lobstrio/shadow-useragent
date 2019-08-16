shadow-useragent
==============

Shadow UserAgent gives you access to the most commonly used UserAgents on the Internet, safe from outdated data.

Behold, the power of UserAgent: 
```python3
>>> import shadow_useragent
>>> ua = shadow_useragent.ShadowUserAgent()
>>> ua.percent(0.05)
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
>>> ua.most_common
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
```

The percent of use is updated on a day-to-day basis, based on the UserAgent of the user of this package. Use is thus dinamically updated, and never outdated. No more unused header that reveals your true identity, you are protected by the group.

Besides, you can rely on traditional features, like picking an header from outstanding IE browser family.


Feature Support
------------

Shadow UserAgent is the only safe, and updated user-agent package.

* UserAgent Percentage of Use
* Day-to-day Update
* Exhaustive UserAgents Family
* Elegant @property Methods
* Community-Based Package

Shadow UserAgent supports Python 2.7 & 3.4–3.7, and runs great on PyPy.

Installation
------------

To install Shadow UserAgent, simply use pipenv (or pip, of course):

```shell
$ pip install shadow-useragent
👻  
```

Never disappointed.

Usage
-----
```python

    from shadow_useragent import ShadowUserAgent
    shadow_useragent = ShadowUserAgent()

     print(shadow_useragent.firefox)
     # Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0
     print(shadow_useragent.chrome)
     # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
     print(shadow_useragent.safari)
     # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
     print(shadow_useragent.edge)
     # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134
     print(shadow_useragent.ie)
     # Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
     print(shadow_useragent.android)
     # Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
     print(shadow_useragent.ipad)
     # Mozilla/5.0 (iPad; CPU OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1
     print(shadow_useragent.random)
     # Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
     
     print(shadow_useragent.random_nomobile)
     # Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36

    # and the best one, random via real world browser usage statistic
    print(ua.random)
    # Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36

    # if you want to excluse mobiles (some websites will display different pages)
    print(shadow_useragent.random_nomobile)
    # Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36

    # if you want a list a all useragents, sorted by most common useragent
    uas = shadow_useragent.get_sorted_uas()
    print(uas)
    """
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
   }, ....
   """
```


