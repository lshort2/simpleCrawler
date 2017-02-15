from urllib.request import urlopen
from urllib import robotparser
from link_finder import LinkFinder
from general import *

class Spider:
    #class variables (share among all instances)
    project_name =''#The name of the project (and the directory where all files are stored)
    base_url     =''#(i.e. the homepage url in order to make relative paths work)
    domain_name  =''#want to make sure we are connecting to a valid domain

    #these are the textfiles
    queue_file   =''#(i.e. thenewboston/queue.txt)
    crawled_file =''
    #these are the variables - they are in RAM as opposed to HDD and much faster to access
    queue   =set()
    crawled =set()
    rp = robotparser.RobotFileParser() #make sure we are allowed to add links


    #ctor/initializer thingy
    #domain_name allows us to use a bunch of cool domain name 
    #fxns to ensure we are connecting to a valid webpage w/o errors
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name =project_name
        Spider.base_url     =base_url
        Spider.domain_name  =domain_name
        Spider.queue_file   =Spider.project_name +'/queue.txt'
        Spider.crawled_file =Spider.project_name +'/crawled.txt'
        self.boot()
        self.rp.set_url(self.base_url +'/robots.txt')
        self.rp.read()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod   #This is a little indicator to python to say, hey this is a static method, (make PEP8 happy)
    def boot():     #  which also means we do not need to pass self in.
        create_project_dir(Spider.project_name)#create directory
        create_data_files(Spider.project_name, Spider.base_url)#create the .txt files
        Spider.queue =file_to_set(Spider.queue_file)
        Spider.crawled =file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name +' crawling ' +page_url)
            print( 'Queue ' + str(len(Spider.queue)) +' | Crawled ' +str(len(Spider.crawled)) )
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()#after we have done our fast operations w/ our variables, now we can update files on HDD

    @staticmethod
    def gather_links(page_url): #need to convert response we get back from zero in bytes to a string,
        html_string =''         # so our python method can actually use it
        try:
            response =urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            findy = LinkFinder(Spider.base_url, page_url)
            findy.feed(html_string)
        except:
            print ('Error: cannot crawl page')
            return set()

        crawlable_links = set()

        for url in findy.page_links():
            if Spider.rp.can_fetch("*", url):
                crawlable_links.add(url)

        return crawlable_links

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue #go to next iteration of loop if we already have url in queue or set
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:   #This means only crawl the site we specified
                continue                        #(not the whole internet)
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)

