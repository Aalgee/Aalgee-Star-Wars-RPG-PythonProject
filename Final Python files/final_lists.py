# FILE: final_list.py
# AUTHOR: Austin Gee
# DATE: 2018-
# DESCRIPTION: This is a module that contains the list creating functions
#   for my final Project
# INPUTS:
# PROCESSES:  
# OUTPUTS:  

import csv

# DESCRIPTION: This function takes a csv file with 4 fields per record and
#   converts it into a list of lists
# INPUTS:
ebe# PROCESSES:
#   for loop
# OUTPUTS:
#   data[](str)

def location_list(file_name):
    data = []
    the_file = open(file_name, "r")
    csv_reader = csv.reader(the_file)
    first = True
    for row in csv_reader:
        if first:
            # ignore this row because it has column headers
            first = False
        else:
            temp = []
            temp.append(row[0]) 
            temp.append(row[1]) 
            temp.append(row[2])
            temp.append(row[3])
            data.append(temp)
    the_file.close
    return data

# DESCRIPTION: This function takes a csv file with 3 fields per record and
#   converts it into a list of lists
# INPUTS:
#   file_name(str)
# PROCESSES:
#   for loop
# OUTPUTS:
#   data[](str)

def quest_item_list(file_name):
    data = []
    the_file = open(file_name, "r")
    csv_reader = csv.reader(the_file)
    first = True
    for row in csv_reader:
        if first:
            # ignore this row because it has column headers
            first = False
        else:
            temp = []
            temp.append(row[0]) # the vendor id as a string
            temp.append(row[1]) # vendor name as a string
            temp.append(row[2])
            data.append(temp)
    the_file.close
    return data

# DESCRIPTION: This function takes a csv file with 2 fields per record and
#   converts it into a list of lists
# INPUTS:
#   file_name(str)
# PROCESSES:
#   for loop
# OUTPUTS:
#   data[](str)

def enemy_list(file_name):
    data = []
    the_file = open(file_name, "r")
    csv_reader = csv.reader(the_file)
    first = True
    for row in csv_reader:
        if first:
            # ignore this row because it has column headers
            first = False
        else:
            temp = []
            temp.append(row[0]) 
            temp.append(row[1])
            data.append(temp)
    the_file.close
    return data

# DESCRIPTION: This function takes a csv file with 3 fields per record and
#   converts it into a list of lists
# INPUTS:
#   file_name(str)
# PROCESSES:
#   for loop
# OUTPUTS:
#   data[](str)

def motivation_list(file_name):
    data = []
    the_file = open(file_name, "r")
    csv_reader = csv.reader(the_file)
    first = True
    for row in csv_reader:
        if first:
            # ignore this row because it has column headers
            first = False
        else:
            temp = []
            temp.append(row[0]) 
            temp.append(row[1]) 
            temp.append(row[2])
            data.append(temp)
    the_file.close
    return data

