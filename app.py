#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib

url='http://127.0.0.1:48080/v1/ping' # isaaxd server ping request
req=urllib.urlopen(url)
print("Hello, Isaax! status code:", req.getcode())

print("Bye!")
