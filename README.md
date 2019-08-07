shadow-useragent
==============

Always keep your user-agent updated with the most recent and most common user-agents

This package will always give you the most commonly used useragents in the web.
This is a python3 wrapper of this free and unlimited API : <http://51.158.74.109/useragents/?format=json>
This api displays usergants that we collect from user of our website (<https://en.lobstr.io>) and other websites from our partners
This technique will let you  enjoy the most recent and most commonly used useragents in the world ! 


Features
********

* grabs up to date and most commonly used ``useragent`` from <http://51.158.74.109/useragents/?format=json/>
* randomize with real world users from <https://en.lobstr.io/> and many others

Installation
------------

```shell

    pip install shadow-useragent
```

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

```


