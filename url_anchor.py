#!/usr/bin/python

import re

def remove_url_anchor(url):
    return re.split("#", url, 1)[0]


print remove_url_anchor("testing#blah")