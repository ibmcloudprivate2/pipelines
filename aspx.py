#!/usr/bin/env python3
import errno, sys
import argparse
from bs4 import BeautifulSoup

'''
to create a script to search in aspxfile for domain, name
'''

parser = argparse.ArgumentParser(description='match domain and name in aspx file')
parser.add_argument('aspxFile', type=str, help='the aspx file')
parser.add_argument('domain', type=str, help='the domain name to be matched')
parser.add_argument('name', type=str, help='the name to be matched')

try:
    args = parser.parse_args()

    aspxfile = args.aspxFile
    domain = args.domain 
    name = args.name 
    print("name : ",name)

    fp = None

    with open(aspxfile) as fp:
        soup = BeautifulSoup(fp)

    # print(soup.prettify())

    foundDomain = False
    foundName = False

    for href in soup.find_all('a'):
        print(href)
        attrs = href["href"].split("?")
        print(attrs)
        if(len(attrs) == 2 and domain == attrs[1]):
            foundDomain = True
        if(name == href.contents[0]):
            foundName = True
        print(href.contents[0])
        if(foundDomain and foundName):
            print("found domain and name")
            break;
    

except Exception as e:
        print(e)
finally:
    fp.close()
    if(foundDomain and foundName):
        print("match found for {0} and {1}".format(domain, name))
        sys.exit(0)
    else:
        print("no match found for {0} and {1}".format(domain, name))
        sys.exit(1)

    