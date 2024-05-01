#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:46:49 2023

@author: kbillesk
"""
import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return list(reader)

def remove_duplicates(mylist):
    set_list = set(mylist)
    uniquelist = list(set_list)
    return uniquelist

inputfile = 'union_lists.csv'
outputfile = 'unique_list.csv'
inlist = read_csv(inputfile)
print(inlist,len(inlist))
outlist = []
for x in inlist:
    outlist.append(x[0])
print(outlist)
outlist = remove_duplicates(outlist)
print(outlist,len(outlist))    
f = open(outputfile, "w", encoding=('utf8'))
spamwriter = csv.writer(f, delimiter='\n',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#for item in outlist:
spamwriter.writerow(outlist)
f.close()