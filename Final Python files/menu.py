# FILE: menu.py
# AUTHOR: Austin Gee
# DATE: 2018-10-19
# DESCRIPTION: This is a module that holds all of the submenus for my
#   final project
# INPUTS:
# PROCESSES:  
# OUTPUTS:  


import create_files
import append_records
import add_this_to_file
import deactivate_record
import adventure


# DESCRIPTION: This function contains the menu for the record editing options
#   within my final project. This function will let the user change everything
#   about any record in my final project csv files except the headers and the
#   fields. changing names is handled by another menu.
# INPUTS:
#   master_list[](str)
#   edit_menu_choices[](str)
#   edit_records_list_name[](str)
# PROCESSES:
#   while loop
# OUTPUTS:  



def edit_file(master_list, edit_menu_choices, edit_records_list_name,
              edit_type_prompts, header_list, edit_record_prompt_list,
              file_name_list, not_found, menu_prompt, title_list,
              enter_choice):
    menu_done = False
    while menu_done == False:
        print_menu(edit_menu_choices)

        token = input('\n' + menu_prompt)
        if token == '1':
            append_records.append_enemy(master_list[0], edit_records_list_name[0],
                                        edit_type_prompts[0], header_list[0],
                                        edit_record_prompt_list[0], not_found,
                                        file_name_list[0], title_list[0])
        elif token == '2':
            append_records.append_enemy(master_list[1], edit_records_list_name[1],
                                        edit_type_prompts[0], header_list[0],
                                        edit_record_prompt_list[0], not_found,
                                        file_name_list[1], title_list[1])
        elif token == '3':
            append_records.append_enemy(master_list[2], edit_records_list_name[2],
                                        edit_type_prompts[0], header_list[0],
                                        edit_record_prompt_list[0], not_found,
                                        file_name_list[2], title_list[2])
        elif token == '4':
            append_records.append_location(master_list[3], edit_records_list_name[3],
                                           edit_type_prompts[1], edit_type_prompts[2],
                                           edit_type_prompts[3], header_list[1],
                                           edit_record_prompt_list[1], edit_record_prompt_list[2],
                                           edit_record_prompt_list[3], not_found, file_name_list[3],
                                           title_list[3])
        elif token == '5':
            append_records.append_quest_item(master_list[4], edit_records_list_name[4],
                                             edit_type_prompts[4], edit_type_prompts[5],
                                             header_list[2], edit_record_prompt_list[4],
                                             edit_record_prompt_list[5], not_found,
                                             file_name_list[4], title_list[4])
        elif token == '6':
            append_records.append_motivation(master_list[5], edit_records_list_name[5],
                                             edit_type_prompts[6], edit_type_prompts[7],
                                             header_list[3], edit_record_prompt_list[6],
                                             edit_record_prompt_list[7], not_found,
                                             file_name_list[5], title_list[5])

        elif token == '7':
            menu_done = True
        else:
            print(enter_choice)
    return
            


# DESCRIPTION: This function contains the menu for adding entire records to my final project.
#   It allows the user to choose a file to add a record to and then lets the user add said
#   record.
# INPUTS:
#   master_list[](str)
#   add_record_list[](str)
#   add_rec_prompt_list[](str)
#   add_again_prompt[](str)
#   file_name_list[](str)
#   header_list[](str)
#   need_name(str)
#   menu_prompt(str)
# PROCESSES:
#   while loop
# OUTPUTS:  


        
def add_record_to_file(master_list, add_record_list, add_rec_prompt_list, add_again_prompt,
                       file_name_list, header_list, need_name, menu_prompt, title_list,
                       enter_choice):
    menu_done = False
    while menu_done == False:
        print_menu(add_record_list)
        token = input('\n' + menu_prompt)
        if token == '1':
            master_list[0] = add_this_to_file.add_enemy(master_list[0], add_rec_prompt_list[0], add_rec_prompt_list[1],
                                  add_again_prompt, file_name_list[0], header_list[0], need_name,
                                       title_list[0])
        elif token == '2':
            master_list[1] = add_this_to_file.add_enemy(master_list[1], add_rec_prompt_list[0], add_rec_prompt_list[1],
                                      add_again_prompt, file_name_list[1], header_list[0], need_name,
                                       title_list[1])
        elif token == '3':
            master_list[2] = add_this_to_file.add_enemy(master_list[2], add_rec_prompt_list[0], add_rec_prompt_list[1],
                                  add_again_prompt, file_name_list[2], header_list[0], need_name,
                                       title_list[2])
        elif token == '4':
            master_list[3] = add_this_to_file.add_location(master_list[3], add_rec_prompt_list[2],
                                     add_rec_prompt_list[3], add_rec_prompt_list[4],
                                     add_rec_prompt_list[5], add_again_prompt,
                                     file_name_list[3], header_list[1], need_name,
                                          title_list[3])
        elif token == '5':
            master_list[4] = add_this_to_file.add_quest_item(master_list[4], add_rec_prompt_list[6],
                                       add_rec_prompt_list[7], add_rec_prompt_list[8],
                                       add_again_prompt, file_name_list[4],
                                       header_list[2], need_name, title_list[4])

        elif token == '6':
            master_list[5] = add_this_to_file.add_motivation(master_list[5], add_rec_prompt_list[9],
                                       add_rec_prompt_list[10],
                                       add_rec_prompt_list[11],
                                       add_again_prompt, file_name_list[5],
                                       header_list[3], need_name, title_list[5])

        elif token == '7':
            menu_done = True
        else:
            print(enter_choice)


# DESCRIPTION: This function has the menu options that are available for deactivating
#   records within the files of my final project.
# INPUTS:
#   master_list[](str)
#   deactivate_menu_list[](str)
#   header_list[](str)
#   file_name_list][(str)
#   dump_file_list[](str)
#   deactivate_record_prompt(str)
#   del_again_prompt(str)
#   not_found(str)
#   menu_prompt(str)
# PROCESSES:
#   while loop
# OUTPUTS:  



def deactivate_records(master_list, deactivate_menu_list, header_list, file_name_list,
                       dump_file_list, deactivate_record_prompt, del_again_prompt,
                       not_found, menu_prompt, title_list, enter_choice):
    menu_done = False
    while menu_done == False:
        print_menu(deactivate_menu_list)
        token = input('\n' + menu_prompt)
        if token == '1':
            master_list[0] = deactivate_record.deactivate_enemy(master_list[0], header_list[0], file_name_list[0],
                                               dump_file_list[0], deactivate_record_prompt,
                                               del_again_prompt, not_found, title_list[0])
        elif token == '2':
            master_list[1] = deactivate_record.deactivate_enemy(master_list[1], header_list[0], file_name_list[1],
                                                        dump_file_list[1],deactivate_record_prompt,
                                                        del_again_prompt, not_found, title_list[1])
        elif token == '3':
            master_list[2] = deactivate_record.deactivate_enemy(master_list[2],
                                            header_list[0], file_name_list[2],
                                    dump_file_list[2], deactivate_record_prompt,
                                    del_again_prompt, not_found, title_list[2])
        elif token == '4':
            master_list[3] = deactivate_record.deactivate_location(master_list[3],
                                        header_list[1], file_name_list[3], dump_file_list[3],
                                        deactivate_record_prompt, del_again_prompt,
                                                not_found, title_list[3])
        elif token == '5':
            master_list[4] = deactivate_record.deactivate_quest_item(master_list[4],
                                            header_list[2], file_name_list[4],
                                        dump_file_list[4], deactivate_record_prompt,
                                        del_again_prompt, not_found, title_list[4])
        elif token == '6':
            master_list[5] = deactivate_record.deactivate_motivation(master_list[5],
                                                header_list[3], file_name_list[5],
                                        dump_file_list[5], deactivate_record_prompt,
                                        del_again_prompt, not_found, title_list[5])
        elif token == '7':
            menu_done = True
        else:
            print(enter_choice)


        '''elif token == '4':
            master_list[3] = deactivate_record.deactivate_quest_item(master_list[3],
                                        header_list[1], file_name_list[3], dump_file_list[3],
                                        deactivate_record_prompt, del_again_prompt,
                                                not_found, title_list[3])
        elif token == '5':
            master_list[4] = deactivate_record.deactivate_location(master_list[4],
                                            header_list[2], file_name_list[4],
                                        dump_file_list[4], deactivate_record_prompt,
                                        del_again_prompt, not_found, title_list[4])'''





# DESCRIPTION: This is the menu that lets the user start the adventure creator.
# INPUTS:
#   master_list[](str)
#   adv_cr_list[](str)
#   menu_prompt(str)
#   must_have_file(str)
# PROCESSES:
#   while loop
# OUTPUTS:  

            

def create_adventure(master_list, adv_cr_list, adv_cr_menu, menu_prompt, must_have_file,
                     enter_choice):
    del master_list[0][0]
    del master_list[1][0]
    del master_list[2][0]
    del master_list[3][0]
    del master_list[4][0]
    del master_list[5][0]
    menu_done = False
    while menu_done == False:
        print_adv_menu(adv_cr_menu)
        token = input('\n' + menu_prompt)
        if token == '1':
            adventure.adventure_creator(master_list,
                                        adv_cr_list[0], adv_cr_list[1], adv_cr_list[2],
                                        adv_cr_list[3], adv_cr_list[4], adv_cr_list[5],
                                        adv_cr_list[6], adv_cr_list[7], adv_cr_list[8],
                                        adv_cr_list[9], must_have_file)
                                
        elif token == '2':
            menu_done = True
        else:
            print(enter_choice)
    return


# DESCRIPTION: This funtion prints the adventure creator menu list in an
#   organized manner
# INPUTS:
#   the_list[](str)
# PROCESSES:  
# OUTPUTS:  


def print_adv_menu(the_list):
    print('\n', the_list[0], '\n', the_list[1])
    return

    
# DESCRIPTION: This funtion prints several of the menu's list's in an
#   organized manner
# INPUTS:
#   the_list[](str)
# PROCESSES:  
# OUTPUTS:  


def print_menu(the_list):
    print('\n', the_list[0], '\n', the_list[1], '\n', the_list[2], '\n',
          the_list[3], '\n', the_list[4], '\n', the_list[5],
          '\n', the_list[6])
    return


# DESCRIPTION: This funtion prints the main menu's list in an
#   organized manner
# INPUTS:
#   the_list[](str)
# PROCESSES:  
# OUTPUTS:  


def print_main_menu(the_list):
    print('\n', the_list[0], '\n', the_list[1], '\n', the_list[2], '\n',
          the_list[3], '\n',the_list[4],)
    return

















