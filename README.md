# sitemappy
A sitemap generator tool that creates an adjacency list for the analysis and visualization of websites.

```py
from sitemappy import SiteNode, SiteMap

siteMap = SiteMap("https://google.com", "optional/path")
siteMap.create_map(total_iterations=10)

siteMap.adjacency_list```
