import unittest
import sys
sys.path.append("..")
from sitemappy import SiteMap

myurl1 = "https://google.com"
myurl2 = "https://google.com"
mypath = "/Users/Tilley/Downloads/chromedriver"

mymap1 = SiteMap(myurl1, mypath, myurl1, dynamic_pages=False)
mymap1.create_map(total_iterations=100)

# mymap2 = SiteMap(myurl2, mypath, myurl2)
# mymap2.create_map(total_iterations=100)

# mymap3 = SiteMap(myurl1, mypath)
# mymap3.create_map(total_iterations=100)

class TestSpeed(unittest.TestCase):

    # test to see that speed has not fallen
    # 100 nodes should almost always take less than 25 seconds (if network is decent)
    # THIS DEPENDS HIGHLY ON NETWORK failures of this test are normal
    def test_map_max_nodes(self):
        self.assertLess(mymap1.run_time, 25)
        


if __name__ == '__main__':
    unittest.main()