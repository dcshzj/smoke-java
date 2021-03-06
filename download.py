#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Script for downloading the latest release JAR file from a list of GitHub
# repositories. The list of GitHub repositories should be given in the first
# parameter when calling this script.
#
# GitHub repositories should be in the following format (no .git):
# https://github.com/<organization>/<repository>
# Example: https://github.com/actions/checkout
#
# Note: This script assumes that the "jars" directory already exists, and all
# downloaded JAR files will be saved into that directory in this format:
# <organization>-<repository>.jar

import json
import os
import sys
import urllib.request

urlsFilePath = sys.argv[1]
urls = []
count = 0

with open(urlsFilePath) as urlsFile:
    urls = urlsFile.readlines()
    print("Found {0} URLs".format(len(urls)))

os.chdir("jars")

for url in urls:
    parts = url.rstrip().split(" ")
    toDownload = parts[0]
    outputFile = parts[1]

    if not toDownload.endswith('.jar'):
        continue

    urllib.request.urlretrieve(toDownload, outputFile)
    count += 1

print("{0} files downloaded".format(count))
