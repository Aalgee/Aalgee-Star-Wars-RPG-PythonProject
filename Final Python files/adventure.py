# FILE: adventure.py
# AUTHOR: Austin Gee
# DATE: 2018-10-20
# DESCRIPTION: This module holds all of the functions that are responsible
#   for generating the adventure files using all of the othewr files in my
#   final project.
# INPUTS:
# PROCESSES:  
# OUTPUTS:  



import random
import csv



# DESCRIPTION: This function takes a file name from the user and uses it to
#   name and create what I call an adventure file.
# INPUTS:
#   master_list[](str)
#   min_prompt(str)
#   riv_prompt(str)
#   enter_a_number(str)
#   file_prompt(str)
#   min_message(str)
#   riv_message(str)
#   nem_message(str)
#   loc_message(str)
#   q_i_message(str)
#   mot_message(str)
# PROCESSES:  
# OUTPUTS:  


def adventure_creator(master_list, min_prompt,
                      riv_prompt, enter_a_number, file_prompt, min_message,
                      riv_message, nem_message, loc_message, q_i_message,
                      mot_message, must_have_file):
    try:
        file_name = input(file_prompt)  + '.csv'
        adv_list = get_adv_list(master_list[0], master_list[1], master_list[2],
                                master_list[3], master_list[4], master_list[5],
                                min_prompt, riv_prompt, enter_a_number)
        print_adv_list(adv_list, min_message, riv_message, nem_message, loc_message,
                       q_i_message, mot_message)
        write_to_csv(file_name, adv_list)
    except:
        print(must_have_file)
    return


# DESCRIPTION: This function takes a list and several messages and uses them to
#   print the list in a more organized way
# INPUTS:
#   adv_list(str)
#   min_message(str)
#   riv_message(str)
#   nem_message(str)
#   loc_message(str)
#   q_i_message(str)
#   mot_message(str)
# PROCESSES:
#   6 for loops
# OUTPUTS:  


def print_adv_list(adv_list, min_message, riv_message, nem_message, loc_message,
                   q_i_message, mot_message):
    for item in adv_list[0]:
        print(min_message, item[0], '| ', item[1])
    for item in adv_list[1]:
        print(riv_message, item[0], '| ', item[1])
    for item in adv_list[2]:
        print(nem_message, item[0], '| ', item[1])
    for item in adv_list[3]:
        print(loc_message, item[0], '| ', item[1], '| ', item[2], '| ', item[3])
    for item in adv_list[4]:
        print(q_i_message, item[0], '| ', item[1], '| ', item[2])
    for item in adv_list[5]:
        print(mot_message, item[0], '| ', item[1], '| ', item[2])
    return




# DESCRIPTION: This function creates a list out of a number of minions,
#   a number of rivals, a nemesis, a location, a quest item and a motivation.
#   together these items create the adventure list
# INPUTS:
#   minions [](str)
#   rivals[](str)
#   nemeses[](str)
#   locations[](str)
#   quest_items[](str)
#   motivations[](str)
#   min_prompt(str)
#   riv_prompt(str)
#   enter_a_number(str)
# PROCESSES:  
# OUTPUTS:
#   adventure_list[](str)


    
def get_adv_list(minions, rivals, nemeses, locations, quest_items,
                 motivations, min_prompt, riv_prompt, enter_a_number):
    adventure_list = []
    min_amount = number_getter(min_prompt, enter_a_number)
    riv_amount = number_getter(riv_prompt, enter_a_number)
    min_list = mult_getter(minions, min_amount)
    riv_list = mult_getter(rivals, riv_amount)
    nemesis = single_getter(nemeses)
    location = single_getter(locations)
    quest_item = single_getter(quest_items)
    motivation = single_getter(motivations)
    adventure_list.append(min_list)
    adventure_list.append(riv_list)
    adventure_list.append(nemesis)
    adventure_list.append(location)
    adventure_list.append(quest_item)
    adventure_list.append(motivation)
    return adventure_list


# DESCRIPTION: This function takes in two prompts and uses them to get a
#   number from the user
# INPUTS:
#   prompt1(str)
#   prompt2(str)
# PROCESSES:
#   while loop
# OUTPUTS:
#   number(int)



def number_getter(prompt1, prompt2):
    got_number = False
    while got_number == False:
        try:
            number = int(input(prompt1))
            got_number = True
        except:
            print(prompt2)
    return number


# DESCRIPTION:  This function takes a list and an amount in the form of an
#   integer. It then uses these things to randomly choose two items from said
#   list in the form of stuff
# INPUTS:
#   the_list[](str)
#   amount(int)
# PROCESSES:
#   while loop
# OUTPUTS:
#   stuff[](str)


def mult_getter(the_list, amount):
    loops = 0
    stuff = []
    while loops <= amount - 1:
        index = random.randint(0, len(the_list) - 1)
        loops += 1
        stuff.append(the_list[index])
    return stuff


# DESCRIPTION: This function uses a list named thing and then randomly
#   chooses and returns one item out of the list
# INPUTS:
#   thing[](str)
# PROCESSES:  
# OUTPUTS:
#   stuff(str)


def single_getter(thing):
    stuff = []
    index = random.randint(0, len(thing) - 1)
    stuff.append(thing[index])
    return stuff



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

