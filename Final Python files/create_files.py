# FILE: create_file.py
# AUTHOR: Austin Gee
# DATE: 2018-10-16
# DESCRIPTION: This module holds functions that create new files for
#   my final project.
# INPUTS:
# PROCESSES:  
# OUTPUTS:  

import csv

    
# DESCRIPTION: this function takes a file name and a list and creates a
#   file
# INPUTS:
#   file_name(str)
#   data_list[[]](str)
# PROCESSES:  
# OUTPUTS:  


def write_to_csv(file_name, data_list):
    out_file = open(file_name, "w", newline="")
    csv_writer = csv.writer(out_file)
    csv_writer.writerows(data_list)
    out_file.close()
    return


# DESCRIPTION: This function takes in a file name and uses it to create
#   a new file
# INPUTS:
#   file_name(str)
# PROCESSES:  
# OUTPUTS:  


def create_enemy_file(file_name):
    the_list = [['Name', 'Type']]
    write_to_csv(file_name, the_list)
    return


# DESCRIPTION: This function takes in a file name and uses it to create
#   a new file
# INPUTS:
#   file_name(str)
# PROCESSES:  
# OUTPUTS:  


def create_location_file(file_name):
    the_list = [['Name', 'Solar System', 'Galactic Location', 'Location Type']]
    write_to_csv(file_name, the_list)
    return


# DESCRIPTION: This function takes in a file name and uses it to create
#   a new file
# INPUTS:
#   file_name(str)
# PROCESSES:  
# OUTPUTS:  


def create_quest_item_file(file_name):
    the_list = [['Name', 'Type', 'Description']]
    write_to_csv(file_name, the_list)
    return


# DESCRIPTION: This function takes in a file name and uses it to create
#   a new file
# INPUTS:
#   file_name(str)
# PROCESSES:  
# OUTPUTS:  


def create_motivation_file(file_name):
    the_list = [['Name', 'Category', 'Description']]
    write_to_csv(file_name, the_list)
    return


