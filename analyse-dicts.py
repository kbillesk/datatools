#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:37:07 2023

@author: kbillesk
"""

import os
import pandas as pd

# Directory containing the CSV files
csv_directory = "dictionaries"  # Replace with the path to your directory

# Initialize an empty DataFrame to store the concatenated data
concatenated_data = pd.DataFrame()

# List all CSV files in the directory
csv_files = [file for file in os.listdir(csv_directory) if file.endswith(".csv")]

# Loop through each CSV file and concatenate its data
for csv_file in csv_files:
    file_path = os.path.join(csv_directory, csv_file)
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Concatenate the data to the existing DataFrame
    concatenated_data = pd.concat([concatenated_data, df], ignore_index=True)
    print(concatenated_data.count())
# Find and extract duplicates based on the first field
#duplicates_data = concatenated_data[concatenated_data.duplicated(subset=concatenated_data.columns[0], keep="first")]
concatenated_data.drop(['languageId'], axis=1, inplace=True)
cleansed_data = concatenated_data.drop_duplicates(subset=['label', 'entryTypeId'])
print("cleaning:")
print(cleansed_data.count())
duplicates_data = cleansed_data[cleansed_data.duplicated(subset="label",keep=False)]
print(duplicates_data.count())
sorted_data = duplicates_data.sort_values(by=['label'])
print(sorted_data.count())
#duplicates_data = df[df.duplicated(subset=['label', 'entryTypeID'], keep=False)]
pivoted_df = sorted_data.pivot(index='label', columns='entryTypeId', values='entryTypeId')
# Write the duplicates to a separate CSV file
print(pivoted_df)
duplicates_data.to_csv("duplicatesall4.csv", index=False)
pivoted_df.to_csv("pivot.csv", index=False)
#concatenated_data.to_csv("alldicts.csv", index=False)

# Now, 'concatenated_data' contains all data, and 'duplicates_data' contains the duplicate rows
#print("Concatenated Data:")
#print(concatenated_data)

#print("\nDuplicate Data:")
#print(duplicates_data)