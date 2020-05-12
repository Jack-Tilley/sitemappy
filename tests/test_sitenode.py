import unittest
import sys
sys.path.append("..")
from sitemappy import SiteNode


mynode = SiteNode('https://127.0.0.1')
mynode.set_ip()

class TestSiteNode(unittest.TestCase):
    # test to see we get the correct ip
    def test_ip(self):
        self.assertEqual(mynode.ip, '127.0.0.1')

    # test to see that our url is correct
    def test_url(self):
        self.assertEqual(mynode.curr_url, '127.0.0.1')
    
    
        
        



if __name__ == '__main__':
    unittest.main()