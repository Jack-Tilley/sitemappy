# sitemappy
A sitemap generator tool that creates a representation of site's network graph for the analysis and visualization of websites.

sitemappy allows you to quickly generate sitemaps and easily transform them to the most popularly used graph formats including weighted and unweighted adjacency lists, adjacency matrices, and node and edge tuples. There's no need to manually reformat graphs to different types as sitemappy can do it for you.

#### Example Usage:
```py
from sitemappy import SiteNode, SiteMap

siteMap = SiteMap("https://google.com", "optional/path")
siteMap.create_map(total_iterations=3)

print(siteMap.adjacency_list)
```
#### Output:
```js
[
    {
        "https://google.com": {
            "https://google.com/preferences?hl=en": 1,
            "https://google.com/advanced_search?hl=en&authuser=0": 1,
            "https://google.com/intl/en/ads/": 1,
            "https://google.com/services/": 1,
            "https://google.com/intl/en/about.html": 1,
            "https://google.com/intl/en/policies/privacy/": 1,
            "https://google.com/intl/en/policies/terms/": 1
        }
    },
    {
        "https://google.com/preferences?hl=en": {
            "https://google.com/webhp?tab=ww": 2,
            "https://google.com/support/websearch?p=ws_cookies_notif&hl=en": 1,
            "https://google.com//support.google.com/websearch?p=ws_settings_safesearch&hl=en": 1,
            "https://google.com/history/optout?hl=en": 1,
            "https://google.com//support.google.com/accounts/answer/61416?hl=en": 1,
            "https://google.com/url?q=https://support.google.com/websearch/%3Fp%3Dws_results_help%26hl%3Den%26fg%3D1&sa=U&ved=0ahUKEwiugJXmn6_pAhWmx4UKHbeJBVoQ8KwCCAI&usg=AOvVaw3KiFEMzsxNB94CU18P43ER": 1,
            "https://google.com/url?q=https://policies.google.com/privacy%3Ffg%3D1&sa=U&ved=0ahUKEwiugJXmn6_pAhWmx4UKHbeJBVoQ8awCCAM&usg=AOvVaw2mMRMD1k9oAjCBu36J9p6a": 1,
            "https://google.com/url?q=https://policies.google.com/terms%3Ffg%3D1&sa=U&ved=0ahUKEwiugJXmn6_pAhWmx4UKHbeJBVoQ8qwCCAQ&usg=AOvVaw17FGmzbsfFI3hEU3lQR4Hx": 1
        }
    },
    {
        "https://google.com/advanced_search?hl=en&authuser=0": {
            "https://google.com/preferences?hl=en": 2,
            "https://google.com/?hl=en": 1,
            "https://google.com//support.google.com/websearch?p=adv_safesearch&hl=en": 2,
            "https://google.com//support.google.com/websearch?p=ws_images_usagerights&hl=en": 1,
            "https://google.com//support.google.com/websearch?p=adv_pages_similar&hl=en": 1,
            "https://google.com//support.google.com/websearch?p=adv_pages_visited&hl=en": 1,
            "https://google.com//support.google.com/websearch?p=adv_operators&hl=en": 1,
            "https://google.com/url?q=https://support.google.com/websearch/%3Fp%3Dws_results_help%26hl%3Den%26fg%3D1&sa=U&ved=0ahUKEwj3grDmn6_pAhX3l3IEHXWiAqQQ8KwCCAE&usg=AOvVaw3sKk-eJiJs2mzCZIsIhCgV": 1,
            "https://google.com/url?q=https://policies.google.com/privacy%3Ffg%3D1&sa=U&ved=0ahUKEwj3grDmn6_pAhX3l3IEHXWiAqQQ8awCCAI&usg=AOvVaw1j6rVmV33eoLfp3_wzBtik": 1,
            "https://google.com/url?q=https://policies.google.com/terms%3Ffg%3D1&sa=U&ved=0ahUKEwj3grDmn6_pAhX3l3IEHXWiAqQQ8qwCCAM&usg=AOvVaw2DpjifAnKTWmGuicTKDpd5": 1
        }
    }
]
```

## Different Graph Types
There are many different ways that graphs can be represented in code, and unfortunately, computers are very picky about which graph representation type you use. Luckily for you, sitemappy's built-in features allow you to use whichever graph representation type you want whenver you want.

```py
from sitemappy import SiteNode, SiteMap

siteMap = SiteMap("https://google.com", "optional/path")
siteMap.create_map(total_iterations=3)

weighted_adj_list = siteMap.adjacency_list
unweighted_adj_list = siteMap.get_unweighted_adjacency_list()
nodes_and_links = siteMap.get_nodes_and_links()
adj_matrix = siteMap.get_adj_matrix()
```


## sitemappy Module Installation
The recommended way to install `sitemappy` is via pip:
```console
$ pip install sitemappy
Collecting sitemappy
...
Installing collected packages: sitemappy
Successfully installed sitemappy-0.x
```

## Documentation
Documentation can be found inside the code in the form of comments. 

(Standalone documentation coming soon...)
