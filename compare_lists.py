#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:26:32 2023

@author: kbillesk
"""

import csv
from collections import Counter

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return list(reader)
    
def find_common_items(file1, file2):
    list1 = read_csv(file1)
    list2 = read_csv(file2)
    print(file1_path,len(list1))
    print(file2_path,len(list2))
    common_items = [item for item in list1 if item in list2]
    #common_items = sorted(list1) == sorted(list2)
    return common_items

# Example usage
outputfile = 'union_lists.csv'
file1_path = 'sharepoint_custodians.csv'  # Replace with the path to your first CSV file
file2_path = 'all_vestas_users.csv'  # Replace with the path to your second CSV file
print("hello")
common_items = find_common_items(file1_path, file2_path)
#unique_items = remove_duplicates(common_items)
print("Common items",len(common_items))
f = open(outputfile, "w", encoding=('utf8'))
spamwriter = csv.writer(f, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
for item in common_items:
    spamwriter.writerow(item)
f.close()