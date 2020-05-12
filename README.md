# sitemappy
A sitemap generator tool that creates an adjacency list for the analysis and visualization of websites.


```py
from sitemappy import SiteNode, SiteMap

siteMap = SiteMap("https://google.com", "optional/path")
siteMap.create_map(total_iterations=10)

siteMap.adjacency_list
```

```[{'url': 'https://google.com', 'url_links': [{'url_link': 'https://google.com/preferences?hl=en', 'times_linked': 1}, {'url_link': 'https://google.com/advanced_search?hl=en&authuser=0', 'times_linked': 1}, {'url_link': 'https://google.com/intl/en/ads/', 'times_linked': 1}, {'url_link': 'https://google.com/services/', 'times_linked': 1}, {'url_link': 'https://google.com/intl/en/about.html', 'times_linked': 1}, {'url_link': 'https://google.com/intl/en/policies/privacy/', 'times_linked': 1}, {'url_link': 'https://google.com/intl/en/policies/terms/', 'times_linked': 1}]}, {'url': 'https://google.com/preferences?hl=en', 'url_links': [{'url_link': 'https://google.com/webhp?tab=ww', 'times_linked': 2}, {'url_link': 'https://google.com/support/websearch?p=ws_cookies_notif&hl=en', 'times_linked': 1}, {'url_link': 'https://google.com//support.google.com/websearch?p=ws_settings_safesearch&hl=en', 'times_linked': 1}, {'url_link': 'https://google.com/history/optout?hl=en', 'times_linked': 1}, {'url_link': 'https://google.com//support.google.com/accounts/answer/61416?hl=en', 'times_linked': 1}, {'url_link': 'https://google.com/url?q=https://support.google.com/websearch/%3Fp%3Dws_results_help%26hl%3Den%26fg%3D1&sa=U&ved=0ahUKEwiTn9usm6_pAhVizoUKHbG4DbkQ8KwCCAI&usg=AOvVaw3JWfd_dUc8PHVXFgUSbTim', 'times_linked': 1}, {'url_link': 'https://google.com/url?q=https://policies.google.com/privacy%3Ffg%3D1&sa=U&ved=0ahUKEwiTn9usm6_pAhVizoUKHbG4DbkQ8awCCAM&usg=AOvVaw2S0Cl6CtH4zwB3ilylG4rT', 'times_linked': 1}, {'url_link': 'https://google.com/url?q=https://policies.google.com/terms%3Ffg%3D1&sa=U&ved=0ahUKEwiTn9usm6_pAhVizoUKHbG4DbkQ8qwCCAQ&usg=AOvVaw2ZLpx2ZaCNaQmp7eSvhoFJ', 'times_linked': 1}]}]
```
