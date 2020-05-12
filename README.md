# sitemappy
A sitemap generator tool that creates an adjacency list for the analysis and visualization of websites.


```py
from sitemappy import SiteNode, SiteMap

siteMap = SiteMap("https://google.com", "optional/path")
siteMap.create_map(total_iterations=3)

print(siteMap.adjacency_list)
```

```
[{'url': 'https://google.com',
  'url_links': [{'times_linked': 1,
                 'url_link': 'https://google.com/preferences?hl=en'},
                {'times_linked': 1,
                 'url_link': 'https://google.com/advanced_search?hl=en&authuser=0'},
                {'times_linked': 1,
                 'url_link': 'https://google.com/intl/en/ads/'},
                {'times_linked': 1, 'url_link': 'https://google.com/services/'},
                {'times_linked': 1,
                 'url_link': 'https://google.com/intl/en/about.html'},
                {'times_linked': 1,
                 'url_link': 'https://google.com/intl/en/policies/privacy/'},
                {'times_linked': 1,
                 'url_link': 'https://google.com/intl/en/policies/terms/'}]},
 {'url': 'https://google.com/preferences?hl=en',
  'url_links': [{'times_linked': 2,
                 'url_link': 'https://google.com/webhp?tab=ww'},
                {'times_linked': 1,
                 'url_link': 'https://google.com/support/websearch?p=ws_cookies_notif&hl=en'},
                {'times_linked': 1,
                 'url_link': 'https://google.com//support.google.com/websearch?p=ws_settings_safesearch&hl=en'},
                {'times_linked': 1,
                 'url_link': 'https://google.com/history/optout?hl=en'},
                {'times_linked': 1,
                 'url_link': 'https://google.com//support.google.com/accounts/answer/61416?hl=en'},
                {'times_linked': 1,
                 'url_link': 'https://google.com/url?q=https://support.google.com/websearch/%3Fp%3Dws_results_help%26hl%3Den%26fg%3D1&sa=U&ved=0ahUKEwj4nrTvm6_pAhWszoUKHbncBj8Q8KwCCAI&usg=AOvVaw3FKhL-0d8aFb3izLht_k2O'},
                {'times_linked': 1,
                 'url_link': 'https://google.com/url?q=https://policies.google.com/privacy%3Ffg%3D1&sa=U&ved=0ahUKEwj4nrTvm6_pAhWszoUKHbncBj8Q8awCCAM&usg=AOvVaw0o2rWxtzV71rmfE5VXeVz4'},
                {'times_linked': 1,
                 'url_link': 'https://google.com/url?q=https://policies.google.com/terms%3Ffg%3D1&sa=U&ved=0ahUKEwj4nrTvm6_pAhWszoUKHbncBj8Q8qwCCAQ&usg=AOvVaw2Cm4TZ16o-HVlapkhTVr_s'}]}]
```
