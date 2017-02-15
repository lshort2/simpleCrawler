#!/usr/bin/env python3
#FotP:
#  Dim lights reduce your appetite.

import threading
from queue import Queue

from spider import Spider
from domain import *
from general import *

#There are no built-in constants, but the python convention is to put in all caps if you don't want to change them
PROJECT_NAME = input('Enter value for PROJECT_NAME\n')
HOMEPAGE = input('Enter value for HOMEPAGE\n')
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME +'/queue.txt'
CRAWLED_FILE = PROJECT_NAME +'/crawled.txt'
NUMBER_OF_THREADS =4 #Not sure max number of threads for my computer, so just start w/ 4

threadQueue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)#first spider will get all the links from the homepage
print('first spider created')

#Create worker threads (will die when main exits)
def create_spiders():
    for _ in range(NUMBER_OF_THREADS):      #convention is to use underscore when we
        t = threading.Thread(target=work)   # don't need to use variable in the for loop
        t.daemon = True #Ensuring it runs as daemon process and dies when main exits
        t.start()

#Do the next job in the queue
def work():
    while True:
        url = threadQueue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        threadQueue.task_done()


#Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        threadQueue.put(link)
    threadQueue.join()#blocks until all jobs in queue processed
    crawl()


#Check if there are items in the queue, if so, crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links):
        print(str(len(queued_links)) +' links in the queue')
        create_jobs()

create_spiders()
crawl()

