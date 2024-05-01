#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:06:26 2023

@author: kbillesk
"""

import os
inputfile = open('names/CAE1.txt', 'r')
duplicatefile = open('names/CAE2.txt', 'r')
firstlist = list(inputfile)
secondlist = list(duplicatefile)
uniquelist = []
outputfile = open('names/CAEunique.txt','w')
for items in secondlist:
   # print(items)
    if items not in firstlist:
        name = items+'\n'
        outputfile.write(name)
print(uniquelist)



