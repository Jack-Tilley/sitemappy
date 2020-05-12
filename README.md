# sitemappy
A sitemap generator tool that creates an adjacency list for the analysis and visualization of websites.


```py
from sitemappy import SiteNode, SiteMap

siteMap = SiteMap("https://google.com", "optional/path")
siteMap.create_map(total_iterations=10)

siteMap.adjacency_list
```

```[{'url': 'https://google.com', 'url_links': [{'url_link': 'https://google.com/preferences?hl=en', 'times_linked': 1}, {'url_link': 'https://google.com/advanced_search?hl=en&authuser=0', 'times_linked': 1}, {'url_link': 'https://google.com/intl/en/ads/', 'times_linked': 1}, {'url_link': 'https://google.com/services/', 'times_linked': 1}, {'url_link': 'https://google.com/intl/en/about.html', 'times_linked': 1}, {'url_link': 'https://google.com/intl/en/policies/privacy/', 'times_linked': 1}, {'url_link': 'https://google.com/intl/en/policies/terms/', 'times_linked': 1}]}, {'url': 'https://google.com/preferences?hl=en', 'url_links': [{'url_link': 'https://google.com/webhp?tab=ww', 'times_linked': 2}, {'url_link': 'https://google.com/support/websearch?p=ws_cookies_notif&hl=en', 'times_linked': 1}, {'url_link': 'https://google.com//support.google.com/websearch?p=ws_settings_safesearch&hl=en', 'times_linked': 1}, {'url_link': 'https://google.com/history/optout?hl=en', 'times_linked': 1}, {'url_link': 'https://google.com//support.google.com/accounts/answer/61416?hl=en', 'times_linked': 1}, {'url_link': 'https://google.com/url?q=https://support.google.com/websearch/%3Fp%3Dws_results_help%26hl%3Den%26fg%3D1&sa=U&ved=0ahUKEwibuuL3mq_pAhVRzBoKHWE5DKwQ8KwCCAI&usg=AOvVaw3V6_Wsppi4xXn1SqmA3wqu', 'times_linked': 1}, {'url_link': 'https://google.com/url?q=https://policies.google.com/privacy%3Ffg%3D1&sa=U&ved=0ahUKEwibuuL3mq_pAhVRzBoKHWE5DKwQ8awCCAM&usg=AOvVaw3UQoKmuVibYRdj4idmZBqO', 'times_linked': 1}, {'url_link': 'https://google.com/url?q=https://policies.google.com/terms%3Ffg%3D1&sa=U&ved=0ahUKEwibuuL3mq_pAhVRzBoKHWE5DKwQ8qwCCAQ&usg=AOvVaw0o5CmeCWU7pHh3k-uAi9QI', 'times_linked': 1}]}, {'url': 'https://google.com/advanced_search?hl=en&authuser=0', 'url_links': [{'url_link': 'https://google.com/preferences?hl=en', 'times_linked': 2}, {'url_link': 'https://google.com/?hl=en', 'times_linked': 1}, {'url_link': 'https://google.com//support.google.com/websearch?p=adv_safesearch&hl=en', 'times_linked': 2}, {'url_link': 'https://google.com//support.google.com/websearch?p=ws_images_usagerights&hl=en', 'times_linked': 1}, {'url_link': 'https://google.com//support.google.com/websearch?p=adv_pages_similar&hl=en', 'times_linked': 1}, {'url_link': 'https://google.com//support.google.com/websearch?p=adv_pages_visited&hl=en', 'times_linked': 1}, {'url_link': 'https://google.com//support.google.com/websearch?p=adv_operators&hl=en', 'times_linked': 1}, {'url_link': 'https://google.com/url?q=https://support.google.com/websearch/%3Fp%3Dws_results_help%26hl%3Den%26fg%3D1&sa=U&ved=0ahUKEwiRyPz3mq_pAhU-hHIEHa4RCL8Q8KwCCAE&usg=AOvVaw1SkgF-tdW-oiGUvRSVCuoj', 'times_linked': 1}, {'url_link': 'https://google.com/url?q=https://policies.google.com/privacy%3Ffg%3D1&sa=U&ved=0ahUKEwiRyPz3mq_pAhU-hHIEHa4RCL8Q8awCCAI&usg=AOvVaw1RRnAUyi5sabcSkNjbcJnD', 'times_linked': 1}, {'url_link': 'https://google.com/url?q=https://policies.google.com/terms%3Ffg%3D1&sa=U&ved=0ahUKEwiRyPz3mq_pAhU-hHIEHa4RCL8Q8qwCCAM&usg=AOvVaw2Ty-2VIAGnjS5P0Ea-Z_P5', 'times_linked': 1}]}, {'url': 'https://google.com/intl/en/ads/', 'url_links': []}, {'url': 'https://google.com/services/', 'url_links': []}, {'url': 'https://google.com/intl/en/about.html', 'url_links': []}, {'url': 'https://google.com/intl/en/policies/privacy/', 'url_links': []}, {'url': 'https://google.com/intl/en/policies/terms/', 'url_links': []}, {'url': 'https://google.com/webhp?tab=ww', 'url_links': [{'url_link': 'https://google.com/preferences?hl=en', 'times_linked': 1}, {'url_link': 'https://google.com/advanced_search?hl=en&authuser=0', 'times_linked': 1}, {'url_link': 'https://google.com/intl/en/ads/', 'times_linked': 1}, {'url_link': 'https://google.com/services/', 'times_linked': 1}, {'url_link': 'https://google.com/intl/en/about.html', 'times_linked': 1}, {'url_link': 'https://google.com/intl/en/policies/privacy/', 'times_linked': 1}, {'url_link': 'https://google.com/intl/en/policies/terms/', 'times_linked': 1}]}, {'url': 'https://google.com/support/websearch?p=ws_cookies_notif&hl=en', 'url_links': [{'url_link': 'https://google.com/?tab=uu', 'times_linked': 2}, {'url_link': 'https://google.com/accounts', 'times_linked': 1}, {'url_link': 'https://google.com/', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/?hl=en', 'times_linked': 2}, {'url_link': 'https://google.com/accounts/community?hl=en', 'times_linked': 2}, {'url_link': 'https://google.com//myaccount.google.com/', 'times_linked': 2}, {'url_link': 'https://google.com//www.google.com/intl/en/privacy.html', 'times_linked': 2}, {'url_link': 'https://google.com/chrome/answer/95647', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/32050', 'times_linked': 1}, {'url_link': 'https://google.com/chrome/answer/95464', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/39612', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/?hl=en#topic=3382296', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/27441?hl=en&ref_topic=3382296', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/32040?hl=en&ref_topic=3382296', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/114129?hl=en&ref_topic=3382296', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/6304920?hl=en&ref_topic=3382296', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/58585?hl=en&ref_topic=3382296', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/3265955?hl=en&ref_topic=3382296', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/3118687?hl=en&ref_topic=3382296', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/183723?hl=en&ref_topic=3382296', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/7682439?hl=en&ref_topic=3382296', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/54068?hl=en&ref_topic=3382296', 'times_linked': 1}, {'url_link': 'https://google.com/accounts/answer/2662856?hl=en&ref_topic=3382296', 'times_linked': 1}]}]
```
