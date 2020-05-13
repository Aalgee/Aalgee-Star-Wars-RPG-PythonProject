# FILE: append_records.py
# AUTHOR: Austin Gee
# DATE: 2018-10-16
# DESCRIPTION: This is a module of functions for my final project. The functions
#   here work together to append the current records
# INPUTS:
# PROCESSES:  
# OUTPUTS:  

import csv


# DESCRIPTION:  This function shows the user a set of records and asks
#   the user if they would like to change a single field in that
#   record at a time
# INPUTS:
#   the_list[[]](str)
#   val1(str)
#   val2(str)
#   val3(str)
#   val4(str)
#   header[](str)
#   prompt1(str)
#   prompt2(str)
#   prompt3(str)
#   not_found(str)
#   file_name(str)
# PROCESSES:
#   for loop
# OUTPUTS:
#   the_list[[]](str)


def append_location(the_list, val1, val2, val3, val4, header, prompt1,
                    prompt2, prompt3, not_found, file_name,title):
    print()
    print('\t\t\t\t', '|', title, '|')
    print('\t\t\t\t ', '-' * len(title), '----', sep='')
    print()
    print_location_list(the_list)
    print()
    name = input(val1) # Choose record to change
    try:
        for i in the_list: 
            if name in i:   # find an item in the list 
                name_index = the_list.index(i)  # get the index for the item
        field_index = 1
        the_list = change_value(the_list, prompt1, val2, name_index, field_index)
        field_index = 2
        the_list = change_value(the_list, prompt2, val3, name_index, field_index)
        field_index = 3
        the_list = change_value(the_list, prompt3, val4, name_index, field_index)
        write_to_csv(file_name, the_list)
    except:
        print(not_found)
    return the_list


# DESCRIPTION: This function shows the user a set of records and asks
#   the user if they would like to change a single field in that
#   record at a time
# INPUTS:
#   the_list[[]](str)
#   val1(str)
#   val2(str)
#   header[](str)
#   prompt1(str)
#   not_found(str)
#   file_name(str)
# PROCESSES:
#   for loop
# OUTPUTS:
#   the_list[](str)


def append_enemy(the_list, val1, val2, header, prompt1, not_found, file_name,
                 title):
    print()
    print('\t\t\t\t', '|', title, '|')
    print('\t\t\t\t ', '-' * len(title), '----', sep='')
    print()
    print_enemy_list(the_list)
    print()
    name = input(val1) # Choose record to change
    try:
        for i in the_list: 
            if name in i:   # find an item in the list 
                name_index = the_list.index(i)  # get the index for the item        
        field_index = 1
        the_list = change_value(the_list, prompt1, val2, name_index, field_index)
        write_to_csv(file_name, the_list)
    except:
        print(not_found)    
    return the_list


# DESCRIPTION:  This function shows the user a set of records and asks
#   the user if they would like to change a single field in that
#   record at a time
# INPUTS:
#   the_list[[]](str)
#   val1(str)
#   val2(str)
#   val3(str)
#   header[](str)
#   prompt1(str)
#   prompt2(str)
#   not_found(str)
#   file_name(str)
# PROCESSES:
#   for loop
# OUTPUTS:
#   the_list[[]](str)



def append_quest_item(the_list, val1, val2, val3, header, prompt1, prompt2, not_found,
                      file_name, title):
    print()
    print('\t\t\t\t', '|', title, '|')
    print('\t\t\t\t ', '-' * len(title), '----', sep='')
    print()
    print_quest_item_list(the_list)
    print()
    name = input(val1) # Choose record to change
    try:
        for i in the_list: 
            if name in i:   # find an item in the list 
                name_index = the_list.index(i)  # get the index for the item        
        field_index = 1
        the_list = change_value(the_list, prompt1, val2, name_index, field_index)
        field_index = 2
        the_list = change_value(the_list, prompt2, val3, name_index, field_index)
        write_to_csv(file_name, the_list)
    except:
        print(not_found)    
    return the_list


# DESCRIPTION:  This function shows the user a set of records and asks
#   the user if they would like to change a single field in that
#   record at a time
# INPUTS:
#   the_list[[]](str)
#   val1(str)
#   val2(str)
#   val3(str)
#   header[](str)
#   prompt1(str)
#   prompt2(str)
#   not_found(str)
#   file_name(str)
# PROCESSES:
#   for loop
# OUTPUTS:
#   the_list[[]](str)



def append_motivation(the_list, val1, val2, val3, header, prompt1, prompt2, not_found,
                      file_name, title):
    print()
    print('\t\t\t\t', '|', title, '|')
    print('\t\t\t\t ', '-' * len(title), '----', sep='')
    print()
    print_motivation_list(the_list)
    print()
    name = input(val1) # Choose record to change
    try:
        for i in the_list: 
            if name in i:   # find an item in the list 
                name_index = the_list.index(i)  # get the index for the item        
        field_index = 1
        the_list = change_value(the_list, prompt1, val2, name_index, field_index)
        field_index = 2
        the_list = change_value(the_list, prompt2, val3, name_index, field_index)
        write_to_csv(file_name, the_list)
    except:
        print(not_found)    
    return the_list


# DESCRIPTION: This program takes a two dimensional list and prints it as a table
# INPUTS:
#   the_list[[]](str)
# PROCESSES:
#   for loop
# OUTPUTS:


def print_motivation_list(the_list):
    line = 'first'      # labeling the first line for header reasons
    for i in the_list:  # Print list and add formatting
        print(format(i[0], '15'), '|', format(i[1], '10'), '|',
              format(i[2], '20'))
        if line == 'first':     # add 65 -'s under header
            print('-'*80)
            line = 'butts'
    return

# DESCRIPTION: This program takes a two dimensional list and prints it as a table
# INPUTS:
#   the_list[[]](str)
# PROCESSES:
#   for loop
# OUTPUTS:

    

def print_quest_item_list(the_list):
    line = 'first'      # labeling the first line for header reasons
    for i in the_list:  # Print list and add formatting
        print(format(i[0], '25'), '|', format(i[1], '15'), '|',
              format(i[2], '20'))
        if line == 'first':     # add 65 -'s under header
            print('-'*80)
            line = 'butts'
    return


# DESCRIPTION: This program takes a two dimensional list and prints it as a table
# INPUTS:
#   the_list[[]](str)
# PROCESSES:
#   for loop
# OUTPUTS:



def print_location_list(the_list):
    line = 'first'      # labeling the first line for header reasons
    for i in the_list:  # Print list and add formatting
        print(format(i[0], '18'), '|', format(i[1], '20'), '|',
              format(i[2], '17'),'|', format(i[3], '20'))
        if line == 'first':     # add 80 -'s under header
            print('-'*80)
            line = 'butts'
    return


# DESCRIPTION: This program takes a two dimensional list and prints it as a table
# INPUTS:
#   the_list[[]](str)
# PROCESSES:
#   for loop
# OUTPUTS:


def print_enemy_list(the_list):
    line = 'first'      # labeling the first line for header reasons
    for i in the_list:  # Print list and add formatting
        print(format(i[0], '35'), '|', format(i[1], '25'))
        if line == 'first':     # add 65 -'s under header
            print('-'*80)
            line = 'butts'
    return


# DESCRIPTION: This function asks athe user if they want to change a field and if they
#   say yes it allows them to do so
# INPUTS:
#   the_list[[]](str)
#   prompt1(str)
#   val(str)
#   name_index(int)
#   field_index(int)
# PROCESSES:  
# OUTPUTS:
#   the_list[[]](str)


def change_value(the_list, prompt1, val, name_index, field_index):
    change_val1 = input(prompt1)
    if change_val1 == 'y' or change_val1 == 'Y':
        new_value = input(val)   
        the_list[name_index][field_index] = new_value 
    return the_list


# DESCRIPTION: This program takes a two dimensional list and writes them to a
#   .csv file
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


