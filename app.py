#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib

url='http://127.0.0.1:48080' # isaaxd server
req=urllib.urlopen(url)
print("Hello Isaax!", req.getcode())
