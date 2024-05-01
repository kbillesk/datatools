#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:44:42 2024

@author: kbillesk
"""
# This script takes two csv files as input and writes out the elements in the first csv that is not also in the second file


import csv

# File paths
file_path_1 = 'emails/finance_emails.csv'
file_path_2 = 'emails/legal-emails.csv'
output_file_path = 'emails/unique_to_file1.csv'

# Read the contents of the first file
with open(file_path_1, mode='r', newline='', encoding='utf-8') as file1:
    reader1 = csv.reader(file1)
    file1_rows = set(row[0] for row in reader1)

# Read the contents of the second file
with open(file_path_2, mode='r', newline='', encoding='utf-8') as file2:
    reader2 = csv.reader(file2)
    file2_rows = set(row[0] for row in reader2)

# Find rows unique to the first file
unique_rows = file1_rows - file2_rows

# Write the unique rows to a new CSV file
with open(output_file_path, mode='w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    for row in unique_rows:
        writer.writerow([row])

print(f'Unique rows written to {output_file_path}')