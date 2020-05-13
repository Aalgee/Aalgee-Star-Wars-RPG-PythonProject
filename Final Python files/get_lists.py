# FILE: get_list.py
# AUTHOR: Austin Gee
# DATE: 2018-11-23
# DESCRIPTION: This is a module that contains the list creating functions
#   for my final Project. it also has functions that check to see if the
#   files are already created or not, and if they haven't been then it will
#   create those files
# INPUTS:
# PROCESSES:  
# OUTPUTS:  

import csv
import create_files



# DESCRIPTION: This function trys to convert a csv file into a list. If the
#   file it is looking for does not exist it then creates the appropriate file
#   and turns that csv file into a list
# INPUTS:
#   no_file_list[](str)
# PROCESSES:
#   while loop
# OUTPUTS:
#   minions[](str)


def get_min_list(no_file_list, file_name_list):
    no_file = True
    while no_file == True:
        try:
            minions = enemy_list(file_name_list[0])
            no_file = False
        except:
            print(no_file_list[0])
            create_files.create_enemy_file(file_name_list[0])
    return minions




# DESCRIPTION: This function trys to convert a csv file into a list. If the
#   file it is looking for does not exist it then creates the appropriate file
#   and turns that csv file into a list
# INPUTS:
#   no_file_list[](str)
# PROCESSES:
#   while loop
# OUTPUTS:
#   rivals[](str)


def get_riv_list(no_file_list, file_name_list):
    no_file = True
    while no_file == True:
        try:
            rivals = enemy_list(file_name_list[1])
            no_file = False
        except:
            print(no_file_list[1])
            create_files.create_enemy_file(file_name_list[1])
    return rivals




# DESCRIPTION: This function trys to convert a csv file into a list. If the
#   file it is looking for does not exist it then creates the appropriate file
#   and turns that csv file into a list
# INPUTS:
#   no_file_list[](str)
# PROCESSES:
#   while loop
# OUTPUTS:
#   nemeses[](str)


def get_nem_list(no_file_list, file_name_list):
    no_file = True
    while no_file == True:
        try:
            nemeses = enemy_list(file_name_list[2])
            no_file = False
        except:
            print(no_file_list[2])
            create_files.create_enemy_file(file_name_list[2])
    return nemeses



# DESCRIPTION: This function trys to convert a csv file into a list. If the
#   file it is looking for does not exist it then creates the appropriate file
#   and turns that csv file into a list
# INPUTS:
#   no_file_list[](str)
# PROCESSES:
#   while loop
# OUTPUTS:
#   locations[](str)


def get_loc_list(no_file_list, file_name_list):
    no_file = True
    while no_file == True:
        try:
            locations = location_list(file_name_list[3])
            no_file = False
        except:
            print(no_file_list[3])
            create_files.create_location_file(file_name_list[3])
    return locations



# DESCRIPTION: This function trys to convert a csv file into a list. If the
#   file it is looking for does not exist it then creates the appropriate file
#   and turns that csv file into a list
# INPUTS:
#   no_file_list[](str)
# PROCESSES:
#   while loop
# OUTPUTS:
#   quest_items[](str)


def get_q_i_list(no_file_list, file_name_list):
    no_file = True
    while no_file == True:
        try:
            quest_items = quest_item_list(file_name_list[4])
            no_file = False
        except:
            print(no_file_list[4])
            create_files.create_quest_item_file(file_name_list[4])
    return quest_items





# DESCRIPTION: This function trys to convert a csv file into a list. If the
#   file it is looking for does not exist it then creates the appropriate file
#   and turns that csv file into a list
# INPUTS:
#   no_file_list[](str)
# PROCESSES:
#   while loop
# OUTPUTS:
#   motivations[](str)


def get_mot_list(no_file_list, file_name_list):
    no_file = True
    while no_file == True:
        try:
            motivations = motivation_list(file_name_list[5])
            no_file = False
        except:
            print(no_file_list[5])
            create_files.create_motivation_file(file_name_list[5])
    return motivations




# DESCRIPTION: This function reads a .csv file and converts it into a
#   two dimensional list with 4 rows
# INPUTS:
#   file_name(str)
# PROCESSES:
#   for loop
# OUTPUTS:
#   data[][](str)

def location_list(file_name):
    data = []
    try:
        the_file = open(file_name, "r")
        csv_reader = csv.reader(the_file)
        first = True
        for row in csv_reader:
                temp = []
                temp.append(row[0])
                temp.append(row[1])
                temp.append(row[2])
                temp.append(row[3])
                data.append(temp)
        the_file.close
    except IOError as err:
        print(Err)
    return data

# DESCRIPTION: This function reads a .csv file and converts it into a
#   two dimensional list with 3 rows
# INPUTS:
#   file_name(str)
# PROCESSES:
#   for loop
# OUTPUTS:
#   data[][](str)

def quest_item_list(file_name):
    data = []
    try:
        the_file = open(file_name, "r")
        csv_reader = csv.reader(the_file)
        first = True
        for row in csv_reader:
                temp = []
                temp.append(row[0])
                temp.append(row[1])
                temp.append(row[2])
                data.append(temp)
        the_file.close
    except IOError as err:
        print(Err)
    return data

# DESCRIPTION: This function reads a .csv file and converts it into a
#   two dimensional list with 2 rows
# INPUTS:
#   file_name(str)
# PROCESSES:
#   for loop
# OUTPUTS:
#   data[][](str)

def enemy_list(file_name):
    data = []
    try:
        the_file = open(file_name, "r")
        csv_reader = csv.reader(the_file)
        first = True
        for row in csv_reader:
                temp = []
                temp.append(row[0])
                temp.append(row[1])
                data.append(temp)
        the_file.close
    except IOError as err:
        print(Err)
    return data

# DESCRIPTION: This function reads a .csv file and converts it into a
#   two dimensional list with 3 rows
# INPUTS:
#   file_name(str)
# PROCESSES:
#   for loop
# OUTPUTS:
#   data[][](str)

def motivation_list(file_name):
    data = []
    try:
        the_file = open(file_name, "r")
        csv_reader = csv.reader(the_file)
        first = True
        for row in csv_reader:
                temp = []
                temp.append(row[0])
                temp.append(row[1])
                temp.append(row[2])
                data.append(temp)
        the_file.close
    except IOError as err:
        print(Err)
    return data

