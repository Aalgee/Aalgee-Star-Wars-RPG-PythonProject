# FILE: add_to_file.py
# AUTHOR: Austin Gee
# DATE: 2018-10-16
# DESCRIPTION: This is a module of functions that are used to add records to
#   the various files in my final project
# INPUTS:
# PROCESSES:  
# OUTPUTS:


import csv
import append_records


# DESCRIPTION: This function takes a list of lists and allows the user to
#   add to it and then uses another function to save it to a file
# INPUTS:
#   the_list[[]](str)
#   prompt1(str)
#   prompt2(str)
#   prompt3(str)
#   file_name(str)
#   header[[]](str)
# PROCESSES:
#   while loop
# OUTPUTS:
#   the_list[](str)



def add_enemy(the_list, prompt1, prompt2, prompt3, file_name, header, need_name,
              title):
    again = 'y'
    print()
    print('\t\t\t\t', '|', title, '|')
    print('\t\t\t\t ', '-' * len(title), '----', sep='')
    print()
    append_records.print_enemy_list(the_list)
    while again == 'y' or again == 'Y':
        name = input('\n' + prompt1)
        if name != '':
            type1 = input(prompt2)
            record_list = [[name, type1]]
            the_list = the_list + record_list
            print()
            print('\t\t\t\t', '|', title, '|')
            print('\t\t\t\t ', '-' * len(title), '----', sep='')
            print()
            append_records.print_enemy_list(the_list)
            write_to_csv(file_name, the_list)
        else:
            print(need_name)
        print()
        again = input(prompt3)
    
    return the_list


# DESCRIPTION: This function takes a list of lists and allows the user to
#   add to it and then uses another function to save it to a file
# INPUTS:
#   the_list[[]](str)
#   prompt1(str)
#   prompt2(str)
#   prompt3(str)
#   prompt4(str)
#   file_name(str)
#   header[[]](str)
# PROCESSES:
#   while loop
# OUTPUTS:
#   the_list[](str)


def add_quest_item(the_list, prompt1, prompt2, prompt3, prompt4, file_name,
                   header, need_name, title):
    again = 'y'
    print()
    print('\t\t\t\t', '|', title, '|')
    print('\t\t\t\t ', '-' * len(title), '----', sep='')
    print()
    append_records.print_quest_item_list(the_list)
    while again == 'y' or again == 'Y':
        name = input('\n' + prompt1)
        if name != '':
            type1 = input(prompt2)
            effect = input(prompt3)
            record_list = [[name, type1, effect]]
            the_list = the_list + record_list
            print()
            print('\t\t\t\t', '|', title, '|')
            print('\t\t\t\t ', '-' * len(title), '----', sep='')
            print()
            append_records.print_quest_item_list(the_list)
            write_to_csv(file_name, the_list)
        else:
            print(need_name)
        print()
        again = input(prompt4)
    
    return the_list


# DESCRIPTION: This function takes a list of lists and allows the user to
#   add to it and then uses another function to save it to a file
# INPUTS:
#   the_list[[]](str)
#   prompt1(str)
#   prompt2(str)
#   prompt3(str)
#   prompt4(str)
#   file_name(str)
#   header[[]](str)
# PROCESSES:
#   while loop
# OUTPUTS:
#   the_list[](str)


def add_motivation(the_list, prompt1, prompt2, prompt3, prompt4, file_name,
                   header, need_name, title):
    again = 'y'
    print()
    print('\t\t\t\t', '|', title, '|')
    print('\t\t\t\t ', '-' * len(title), '----', sep='')
    print()
    append_records.print_motivation_list(the_list)
    while again == 'y' or again == 'Y':
        name = input('\n' + prompt1)
        if name != '':
            type1 = input(prompt2)
            effect = input(prompt3)
            record_list = [[name, type1, effect]]
            the_list = the_list + record_list
            print()
            print('\t\t\t\t', '|', title, '|')
            print('\t\t\t\t ', '-' * len(title), '----', sep='')
            print() 
            append_records.print_motivation_list(the_list)
            write_to_csv(file_name, the_list)
        else:
            print(need_name)
        print()
        again = input(prompt4)
    
    return the_list


# DESCRIPTION: This function takes a list of lists and allows the user to
#   add to it and then uses another function to save it to a file
# INPUTS:
#   the_list[[]](str)
#   prompt1(str)
#   prompt2(str)
#   prompt3(str)
#   prompt4(str)
#   prompt5(str)
#   file_name(str)
#   header[[]](str)
# PROCESSES:
#   while loop
# OUTPUTS:
#   the_list[](str)


def add_location(the_list, prompt1, prompt2, prompt3, prompt4, prompt5, file_name,
                   header, need_name, title):
    again = 'y'
    print()
    print('\t\t\t\t', '|', title, '|')
    print('\t\t\t\t ', '-' * len(title), '----', sep='')
    print()
    append_records.print_location_list(the_list)
    while again == 'y' or again == 'Y':
        name = input('\n' + prompt1)
        if name != '':
            sol_sys = input(prompt2)
            gal_loc = input(prompt3)
            loc_type = input(prompt4)
            record_list = [[name, sol_sys, gal_loc, loc_type]]
            the_list = the_list + record_list
            print()
            print('\t\t\t\t', '|', title, '|')
            print('\t\t\t\t ', '-' * len(title), '----', sep='')
            print()
            append_records.print_location_list(the_list)
            write_to_csv(file_name, the_list)
        else:
            print(need_name)
        print()
        again = input(prompt5)
    
    return the_list


# DESCRIPTION: This function takes a list of lists and saves them as a .csv
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


