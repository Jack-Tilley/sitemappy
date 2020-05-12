# Jack Tilley
# January 2020
# The purpose of this module is to scrape the links from a website and find all links that the website contains

from webscraping_tools import ezScrape
from bs4 import BeautifulSoup
import requests
import socket
import time

# a graph containing the links a website has, links in the form of SiteNode
class SiteMap:
    def __init__(self, base_url, path, starting_url=None, this_map=None, local_only=None, dynamic_pages=None):
        self.base_url = base_url  # initial url. ex: https://www.youtube.com
        self.path = path  # path to chrome driver
        self.starting_url = starting_url
        # setting default values
        # dictionary containing UrlNodes
        self.this_map = this_map if this_map is not None else {}
        # where the crawl should start from
        self.starting_url = starting_url if starting_url is not None else base_url
        # should we stay local to this site or allow crossover to other sites
        # True is almost always recommended
        self.local_only = local_only if local_only is not None else True
        # setting this to true will cause the program to run significantly slower
        # but the program scraping will be extremely more accurate
        self.dynamic_pages = dynamic_pages if dynamic_pages is not None else False
        # done setting default vals
        # nodes that we have seen so far and how many times we have seen it
        self.seen_nodes = {self.starting_url: 1}
        self.explored = {}  # explored for bfs
        self.queue = [self.starting_url]  # queue for bfs
        self.adjacency_list = [] # adjacency list representation of pages
        self.iter = 0 # iteration number for bfs
        # timer
        self.run_time = 0
        self.start_time = 0
        self.end_time = 0
        if self.local_only:
            # helps get the number of "/"
            self.end_url_index = len(base_url) - 1
        else:
            self.end_url_index = -2  # this needs to be fixed
        # contains pointers to SiteNode instances where key is url, value is pointer to SiteNode
        self.map_info = {}

        # setting default values for class members of SiteNode class
        SiteNode.dynamically_generated = self.dynamic_pages
        SiteNode.dyna_path = self.path
        SiteNode.base_url = self.base_url

    # finds all the links on the specified url
    def get_links(self, url):
        # creates a root node for the current page
        # gets all links from the html of that page
        this_node = SiteNode(url)
        soup = BeautifulSoup(this_node.html, "html.parser")
        title = soup.find("title")
        links = soup.find_all("a")
        
        # loops through each link we found earlier
        # creates a new node if the format is valid
        for link in links:
            # collects link
            new_node_url = link.get("href")
            # if link is broken or missing, do nothing
            if new_node_url is None:
                continue
            # if node stays within current site
            if new_node_url.startswith("/"):
                new_node_url = self.base_url + new_node_url
             # if node leads to another site
            elif new_node_url.startswith("http"):
                # if we only want links from the current site, we throw away this url
                if self.local_only:
                    continue
                # otherwise we keep the url
                else:
                    new_node_url = new_node_url
             # otherwise we have a unidentified url, do nothing
            else:
                continue

            # adds this link to our seen_nodes dict if its not already there
            # updates node in d3js
            if self.seen_nodes.get(new_node_url, 0) == 0:
                self.seen_nodes[new_node_url] = 1
            else:
                self.seen_nodes[new_node_url] += 1
            
            #  adds new node to our seen collection, inc times seen
            this_node.update_connections(new_node_url)
            # gives the node its title datamember
            this_node.set_title(title)
            ## gives the node its ip
            # this_node.set_ip()
            # if we haven't yet seen this url
            if new_node_url not in self.queue and new_node_url not in self.explored:
                # adds new node to queue to be explore
                self.queue.append(new_node_url)

        # gives the root node its link level
        # this_node.get_link_level()

        # add the node we just explored to our graph
        self.this_map[this_node.curr_url] = this_node.connections
        # adds current node to our explored dictionary
        self.explored[this_node.curr_url] = 1
        # updates our adj list to include this node
        self.update_adjacency_list(this_node)
        # updates our map info with pointer to new node
        self.map_info[this_node.curr_url] = this_node

    # bfs to find all nodes from the given url
    def create_map(self, total_iterations=None):
        self.start_time = time.perf_counter()
        # set default value of total_iterations
        if total_iterations is None:
            total_iterations = 30
        else:
            total_iterations = total_iterations
        # total_iterations usage SHOULD BE UPDATED AS IT IS NOT PROPER STYLE

        # bfs will stop when iteration == total_iterations,
        # if total_iteration is negative we will continue until we have exhausted the queue
        iteration = 0
        while self.queue and iteration != total_iterations:
            current_node_url = self.queue.pop(0)

            # check if url has been explored yet
            if self.explored.get(current_node_url, 0) == 0:
                self.get_links(current_node_url)
                # ATTEMPT TO USE MULTITHREADING HERE

            iteration += 1
        self.end_time = time.perf_counter()
        self.get_time(self.start_time, self.end_time)

    # updates adjacency list with new node
    def update_adjacency_list(self, this_node):
        this_node.adj_list["url"] = this_node.curr_url
        url_links = [{"url_link": key, "times_linked": val}
                     for key, val in this_node.connections.items()]
        this_node.adj_list["url_links"] = url_links
        # this_node.adj_list["url_links"] = this_node.connections
        # this_node.adj_list["files"] = this_node.files
        # this_node.adj_list["ip"] = this_node.ip
        # this_node.adj_list["html"] = this_node.html

        self.adjacency_list.append(this_node.adj_list)

    # returns the map we have created
    def get_map(self):
        return self.this_map

    # Append the execution time
    def get_time(self, start, end):
        t = round(end - start, 2)
        self.run_time = t


# a node containing the links a url contains
# along with other data it might have
class SiteNode:
    # class variables
    dynamically_generated = False
    dyna_path = None
    base_url = None

    def __init__(self, curr_url, html=None):
        self.curr_url = curr_url  # this nodes url
        self.connections = {}  # this nodes outgoing links
        self.files = []  # the filenames in this nodes html
        self.ip = ""  # this nodes ip
        self.adj_list = {}  # this node formattted to json for adjacency list
        self.html = html if html is not None else self.get_html(
            self.curr_url)  # this nodes html
        self.title = ""

    # converts domain name into ip
    def set_ip(self):
        try:
            self.ip = socket.gethostbyname(self.curr_url)
        except UnicodeError:
            self.ip = ""

    # gets html dynamically or non dynamically
    # dynamically contains js loaded elements
    def get_html(self, url):
        if self.dynamically_generated:
            # gets dynamically loaded html
            html = ezScrape.getHTML(self.curr_url, self.dyna_path)
        else:
            # gets regular html
            html = requests.get(self.curr_url).text
        return html

    def set_title(self, title):
        self.title = title


    def update_connections(self, new_node_url):
        self.connections[new_node_url] = self.connections.get(new_node_url, 0) + 1


