#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 07:50:17 2023

@author: kbillesk
"""

import csv
import re

def extract_list(file1):
    with open(file1, 'r') as f1:
        lines1 = [row.split()[0] for row in f1]
      #  reader1 = csv.reader(f1)
      #  lines1 = 
        print('lines:',f1.name,len(lines1))
    return lines1

def find_common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
      #  print('lines2:',len(lines2))
   # common_elements = {}
    common_elements = set1.intersection(set2)
    return list(common_elements)


def compare_csv_identical(lines1, lines2):
    ident_strings = sorted(lines1) == sorted(lines2)
    return ident_strings

if __name__ == '__main__':
    file1 = input('Enter the path to the first csv file: ')
    file2 = input('Enter the path to the second csv file: ')
  #  common_strings = compare_csv_files(extract_list(file1), extract_list(file2))
    common_elements = find_common(extract_list(file1), extract_list(file2))
    ident_strings = compare_csv_identical(extract_list(file1), extract_list(file2))
    #print('Common strings:', common_strings)
    print("Common elements for loop:",common_elements)
    print("are lists identical:",ident_strings)
    print("common elements: set", len(common_elements))