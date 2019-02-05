#!/usr/bin/python

def remove_url_anchor(url):
    return url.split("#")[0]


print remove_url_anchor("www.testing.com#blah?=0")