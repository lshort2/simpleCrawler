#!/usr/bin/env python3
from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    #initializer/ctor
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()#set for us to put links

    def handle_starttag(self, tag, attrs):
        if tag == 'a':                     #Only run this functionality where we have an anchor,
            for(attribute, value) in attrs:#  which should be where the links are
                if (attribute == 'href':   #take care of issue w/ relative paths
                    url =parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):   #HTMLParser says, "Hey every time you inherit from me,
        pass                    # you have to use this method, so i know what to do

