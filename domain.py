#!/usr/bin/env python3

#Fxns responsible for extracting domain name
#Don't crawl the entire internet
from urllib.parse import urlparse

#Get domain name
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] +'.' +results[-1]
    except:
        print('Having trouble getting domain for: ' +url)
        return ''


#Get subdomain name (name.example.com) --> example.com
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        print('Having trouble getting subdomain for: ' +url)
        return ''

