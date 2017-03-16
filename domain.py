#Fxns responsible for extracting domain name
#Don't crawl the entire internet
from urllib.parse import urlparse

#Get domain name
def get_domain_name(url):
    try:
        print('results = ' +get_sub_domain_name(url))
        results = get_sub_domain_name(url).split('.')
        print('len(results): ', len(results))
        if(len(results) > 1):
            print('returning ' +results[-2] +'.' +results[-1])
            return results[-2] +'.' +results[-1]
        else:
            print('returning ' +results[0])
            return results[0]
    except:
        print('Having trouble getting domain for: ' +url)
        print('results[-2] = ' +results[-2])
        print('results[-1] = ' +results[-1])
        return ''


#Get subdomain name (name.example.com) --> example.com
def get_sub_domain_name(url):
    print('SUB BITCHES')
    try:
        #       print('urlparse(url).netloc = ' +urlparse(url).netloc)
               #  sub_domain = urlparse(url).netloc
               #  if(urlparse(url).scheme == ''):
               #     #           print('yo!')
               #      return 'http://' +sub_domain
               #  else:
               #      return sub_domain
        if(urlparse(url).scheme ==''):
            return urlparse('http://' +url).netloc
        else:
            return urlparse(url).netloc
    except:
        print('Having trouble getting subdomain for: ' +url)
        return ''

#Prepends 'http://' scheme to a provided url if no scheme is provided
#This is requried for the robotparser module to read robots.txt
def make_full_url(url):
    try:
        if(urlparse(url).scheme == ''):
            url = 'http://' +url
        return url
    except:
        print('Having trouble generating full length url for: ' +url)
        return ''


