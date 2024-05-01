#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:04:57 2023

@author: kbillesk
"""
import re
import csv


if __name__ == '__main__':
    file1 = input('Enter the path to the csv file: ')
    file2 = input('Enter the name of the outputcsv file: ')
    outputfile = open(file2, 'w')
    with open(file1, 'r') as inputfile:
        spamreader = csv.reader(inputfile, quoting=csv.QUOTE_MINIMAL)
        spamwriter =csv.writer(outputfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in spamreader:
            exten = re.search(r'[A-Za-z0-9].+(\.[A-Za-z0-9]{2,5})', row[0])
            if re.match(r'[A-Za-z0-9].+(\.[A-Za-z0-9]{2,5})', row[0]):
                row.append(exten.group(1))
            else:
                row.append("No_ext")
            spamwriter.writerow(row)
    outputfile.close()        

