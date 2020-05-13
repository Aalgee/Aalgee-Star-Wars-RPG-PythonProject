# FILE: deactivate_record.py
# AUTHOR: Austin Gee
# DATE: 2018-11-23
# DESCRIPTION: This module contains several functions that are used
#   to deactivate records using my final project program
# INPUTS:
# PROCESSES:  
# OUTPUTS:  

import csv
import append_records


# DESCRIPTION: This function is used to delete a record from an enemy file
# it then uses other functions to save those deleted records to a dump file
# INPUTS:
#   the_list[](str)
#   header[](str)
#   file_name1(str)
#   file_name2(str)
#   prompt1(str)
#   again_prompt(str)
#   not_found(str)
# PROCESSES:
#   while loop
#   for loop
# OUTPUTS:
#   the_list[](str)


def deactivate_enemy(the_list, header, file_name1, file_name2, prompt1,
                     again_prompt, not_found, title):
    again = 'y'
    while again == 'y' or again == 'Y':
        print()
        print('\t\t\t\t', '|', title, '|')
        print('\t\t\t\t ', '-' * len(title), '----', sep='')
        print()
        append_records.print_enemy_list(the_list)
        print()
        name = input(prompt1)
        for item in the_list:
            if name in item:
                del_index = the_list.index(item)
                deactivated_record = the_list[del_index]
                the_list.remove(the_list[del_index])
                write_to_csv(file_name1, the_list)
                append_to_csv(file_name2, deactivated_record)
        
        again = input(again_prompt)
                
    return the_list


# DESCRIPTION: This function is used to delete a record from the Quest Item
#   file it then uses other functions to save those deleted records to a
#   dump file
# INPUTS:
#   the_list[](str)
#   header[](str)
#   file_name1(str)
#   file_name2(str)
#   prompt1(str)
#   again_prompt(str)
#   not_found(str)
# PROCESSES:
#   while loop
#   for loop
# OUTPUTS:
#   the_list[](str)


def deactivate_quest_item(the_list, header, file_name1, file_name2, prompt1,
                     again_prompt, not_found, title):
    again = 'y'
    while again == 'y' or again == 'Y':
        print()
        print('\t\t\t\t', '|', title, '|')
        print('\t\t\t\t ', '-' * len(title), '----', sep='')
        print()
        append_records.print_quest_item_list(the_list)
        print()
        name = input(prompt1)
        for item in the_list:
            if name in item:
                del_index = the_list.index(item)
                deactivated_record = the_list[del_index]
                the_list.remove(the_list[del_index])
                write_to_csv(file_name1, the_list)
                append_to_csv(file_name2, deactivated_record)
                
        again = input(again_prompt)
                
    return the_list


# DESCRIPTION: This function is used to delete a record from the Location
#   file it then uses other functions to save those deleted records to a
#   dump file
# INPUTS:
#   the_list[](str)
#   header[](str)
#   file_name1(str)
#   file_name2(str)
#   prompt1(str)
#   again_prompt(str)
#   not_found(str)
# PROCESSES:
#   while loop
#   for loop
# OUTPUTS:
#   the_list[](str)


def deactivate_location(the_list, header, file_name1, file_name2, prompt1,
                     again_prompt, not_found, title):
    again = 'y'
    while again == 'y' or again == 'Y':
        print()
        print('\t\t\t\t', '|', title, '|')
        print('\t\t\t\t ', '-' * len(title), '----', sep='')
        print()
        append_records.print_location_list(the_list)
        print()
        name = input(prompt1)
        for item in the_list:
            if name in item:
                del_index = the_list.index(item)
                deactivated_record = the_list[del_index]
                the_list.remove(the_list[del_index])
                write_to_csv(file_name1, the_list)
                append_to_csv(file_name2, deactivated_record)
                
        again = input(again_prompt)
                
    return the_list


# DESCRIPTION: This function is used to delete a record from the Motivation
#   file it then uses other functions to save those deleted records to a
#   dump file
# INPUTS:
#   the_list[](str)
#   header[](str)
#   file_name1(str)
#   file_name2(str)
#   prompt1(str)
#   again_prompt(str)
#   not_found(str)
# PROCESSES:
#   while loop
#   for loop
# OUTPUTS:
#   the_list[](str)


def deactivate_motivation(the_list, header, file_name1, file_name2, prompt1,
                     again_prompt, not_found, title):
    again = 'y'
    while again == 'y' or again == 'Y':
        print()
        print('\t\t\t\t', '|', title, '|')
        print('\t\t\t\t ', '-' * len(title), '----', sep='')
        print()
        append_records.print_motivation_list(the_list)
        print()
        name = input(prompt1)
        for item in the_list:
            if name in item:
                del_index = the_list.index(item)
                deactivated_record = the_list[del_index]
                the_list.remove(the_list[del_index])
                write_to_csv(file_name1, the_list)
                append_to_csv(file_name2, deactivated_record)
                
        again = input(again_prompt)
    
    return the_list


# DESCRIPTION: This program takes a two dimensional list and writes them to a
#   .csv file
# INPUTS:
#   file_name(str)
#   data_list[](str)
# PROCESSES:  
# OUTPUTS:


def write_to_csv(file_name, data_list):
    out_file = open(file_name, "w", newline="")
    csv_writer = csv.writer(out_file)
    csv_writer.writerows(data_list)
    out_file.close()
    return


# DESCRIPTION: This program takes a two dimensional list and appends
#   them to a .csv file. this is how the dump files are saved
# INPUTS:
#   file_name(str)
#   data_list[](str)
# PROCESSES:  
# OUTPUTS:


def append_to_csv(file_name, data_list):
    out_file = open(file_name, "a", newline="")
    csv_writer = csv.writer(out_file)
    csv_writer.writerow(data_list)
    out_file.close()
    return
