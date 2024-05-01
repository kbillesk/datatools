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


def write_to_file(output_file, data):
    with open(output_file, 'w') as file:
        for item in data:
            file.write(item + '\n')


file1 = 'CPR/full-names-cae-2.csv'
output_file = 'CPR/full-names.csv'
with open(file1, 'r') as f1:
    matching_cpr = []
    csv_file = csv.reader(f1)
    print(csv_file.line_num)
    for row in csv_file:
        for values in row:
            print(values["FULL_NAME"]
            if values.strip() == "FULL_NAME":
                print(values)
                matching_cpr.append(values)
write_to_file(output_file, matching_cpr)
