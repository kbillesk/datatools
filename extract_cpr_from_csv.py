#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 07:50:17 2023

@author: kbillesk
"""

import csv
import re

# def extract_matching_cpr(input_list):
    
#     matching_cpr = []
#     for item in input_list:
#         #print(item)
#         if re.match(regex_pattern, item):
#            matching_cpr.add = re.match(regex_pattern, item)
           
#     #matching_cpr = [item for item in input_list if re.match(regex_pattern, item)]
#     return matching_cpr

def extract_list(file1, policies):
    regex_pattern = '(0[1-9]|[12]\d|3[01])[\/-]?(0[1-9]|1[0-2])[\/-]?\d{2}[- ]?\d{4}'
    print(policies)
    with open(file1, 'r') as f1:
        matching_cpr = []
        for row in f1:
            print("New line")
            print(row)
            thepolicy = [value.strip() for value in policies if value.strip() in row]
            print(thepolicy)
            for item in row.split(","):
                if re.search(regex_pattern, item):
                    cpr = re.search(regex_pattern, item)
                    print(cpr.group())
                    policymatch=False
                    thematch = "Test"
                    for element in policies:
                       #print(element)
                       source = element
                       if len(thepolicy) > 0:
                           if thepolicy[0] in row:
                               policymatch = True
                               thematch = source
                     #   else:
                           # print("not in policy")
                           outputline = thepolicy[0] + ", " + str(cpr.group())
                           print(outputline)
                    if policymatch: matching_cpr.append(outputline)
                #else:             
                    #print(item+" shit")
      #  reader1 = csv.reader(f1)
      #  lines1 = 
        print('lines:',f1.name)
    return matching_cpr

def write_to_file(output_file, data):
    with open(output_file, 'w') as file:
        for item in data:
            file.write(item + '\n')

if __name__ == '__main__':
    file1 = input('Enter the path to the first csv file: ')
    output_file = input('Enter the pathname for the output file: ')
    policy_file = open("CPR/policies03.txt", 'r')
    valid_policies = policy_file.readlines()
    common_elements = extract_list(file1, policies=valid_policies)
    #print('Common strings:', common_strings)
    print(len(common_elements))
    write_to_file(output_file, common_elements)
