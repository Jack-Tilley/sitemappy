# sitemappy
A sitemap generator tool that creates an adjacency list for the analysis and visualization of websites.


```py
from sitemappy import SiteNode, SiteMap

siteMap = SiteMap("https://google.com", "optional/path")
siteMap.create_map(total_iterations=3)

print(siteMap.adjacency_list)
```

```
[{'https://google.com': {'https://google.com/advanced_search?hl=en&authuser=0': 1,
                         'https://google.com/intl/en/about.html': 1,
                         'https://google.com/intl/en/ads/': 1,
                         'https://google.com/intl/en/policies/privacy/': 1,
                         'https://google.com/intl/en/policies/terms/': 1,
                         'https://google.com/preferences?hl=en': 1,
                         'https://google.com/services/': 1}},
 {'https://google.com/preferences?hl=en': {'https://google.com//support.google.com/accounts/answer/61416?hl=en': 1,
                                           'https://google.com//support.google.com/websearch?p=ws_settings_safesearch&hl=en': 1,
                                           'https://google.com/history/optout?hl=en': 1,
                                           'https://google.com/support/websearch?p=ws_cookies_notif&hl=en': 1,
                                           
                                                           ...
                                            
                                           'https://google.com/webhp?tab=ww': 2}},
 {'https://google.com/advanced_search?hl=en&authuser=0': {'https://google.com//support.google.com/websearch                                                                               p=adv_operators&hl=en': 1,}}
]
```
