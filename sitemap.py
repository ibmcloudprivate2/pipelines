#!/usr/bin/env python3
from xml.etree import ElementTree
import errno, sys
import argparse

'''
to create a script to search in xmlfile for title, description
'''

parser = argparse.ArgumentParser(description='match title and description in sitemap file')
parser.add_argument('sitemapFile', type=str, help='the Web.sitemap file')
parser.add_argument('title', type=str, help='the title name to be matched')
parser.add_argument('description', type=str, help='the description to be matched')

args = parser.parse_args()

xmlfile = args.sitemapFile
title = args.title 
desc = args.description 

root = ElementTree.parse(xmlfile).getroot()

print(root.tag)
print(root.attrib)

found = False

for elem in root.iter():
    print(elem.tag, elem.attrib )  
    for attr in elem.attrib:
        print(elem.attrib["title"])
        print(elem.attrib["description"])
        if( title == elem.attrib["title"] and desc == elem.attrib["description"]):
            print("found match")
            found = True

if( found ):
    print("found match ", title, desc)
    sys.exit(0)
else:
    print("not found match ", title, desc)
    sys.exit(1)


# for item in root.findall("item"):
#     ElementTree.dump(item)