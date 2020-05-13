# FILE: star_wars_adventure_creator.py
# DATE: 2018-11-26
# AUTHOR: Austin Gee
# DESCRIPTION:  This is my Final project. It is a menu driven program. Before it
#   all starts the program checks to see if the record containing files exist and
#   then if they do not the program creates them. Using the menu the user can add
#   new records to the files, edit records in the files and deactivate records in
#   the various files. There is also a feature called the adventure creator. This
#   feature asks the user for a file name and a couple of numbers. It then
#   randomly creates the bare bones for an adventure using at least one record
#   from each file.

# import various modules
import get_lists
import append_records
import add_this_to_file
import create_files
import deactivate_record
import menu

def main():
    # Program Title, subtitle, and and description
    title = '****************Star Wars: Force and Destiny****************'
    subtitle = '****************Unofficial Adventure Creator****************'
    program_description = ('\nThis program is a tool that was created to help Game Masters\n'
                           'running the Star Wars: Force and Destiny roleplaying game to\n'
                           'create new adventures. It does this by randomly generating a\n'
                           'list of enemies, locations, quest items, and motivations for\n'
                           'the Game Master to incorporate into their adventure. Of course\n'
                           'before any adventure can be created there needs to be at least\n'
                           'one record in each of the six files used to store Minions,\n'
                           'Rivals, Nemeses, Locations, Quest Items, and Motivations.\n'
                           'Enjoy!!!')


    # The following loose prompts and messages are all general prompts that are not used
    # in any lists and may be used by more than one function
    
    # prompt to continue past the title page
    enter_to_continue = '\nPress Enter to Continue: '

    # prompt used if no value is entered
    need_value = 'Please enter a value.'
    need_name = 'Please enter a name.'

    # add again prompt and delete again prompt
    add_again_prompt = 'Do you want to add some more?(y or n):'
    del_again_prompt = 'Do you want to delete some more?(y or n):'
    
    # deactivate record prompt
    deactivate_record_prompt = 'Type the name of the record you want to delete: '
    
    # item not found message
    not_found = 'The item you searched for was not found'

    # Menu prompt
    menu_prompt = 'Please make a selection: '

    # must have a file error message
    must_have_file = '\nError: You must have at least one record in every file.'

    # please enter your choice message
    enter_choice = 'Please enter a menu choice.'

    # Titles for various displayed tables
    min_title = 'Minions'
    riv_title = 'Rivals'
    nem_title = 'Nemeses'
    loc_title = 'Locations'
    q_i_title = 'Quest Items'
    mot_title = 'Motivations'

    # List of titles for various displayed tables
    title_list = [min_title, riv_title, nem_title,
                  loc_title, q_i_title, mot_title]
    
    
    # csv file names
    minions_file = 'minions.csv'
    rivals_file = 'rivals.csv'
    nemeses_file = 'nemeses.csv'
    locations_file = 'locations.csv'
    quest_items_file = 'quest_items.csv'
    motivations_file = 'motivations.csv'

    #csv file name list
    file_name_list = [minions_file, rivals_file, nemeses_file,
                      locations_file, quest_items_file, motivations_file]
    


    # csv deactivated record dump files
    minions_dump_file = 'minion_dump.csv'
    rivals_dump_file = 'rivals_dump.csv'
    nemeses_dump_file = 'nemeses_dump.csv'
    locations_dump_file = 'locations_dump.csv'
    quest_items_dump_file = 'quest_items_dump.csv'
    motivations_dump_file = 'motivations_dump.csv'

    # csv dump file list
    dump_file_list = [minions_dump_file, rivals_dump_file, nemeses_dump_file,
                      locations_dump_file, quest_items_dump_file,
                      motivations_dump_file]



    # File Headers
    enemy_header = [['Name', 'Type']]
    location_header = [['Name', 'Solar System', 'Galactic Location', 'Location Type']]
    quest_item_header = [['Name', 'Type', 'Effect']]
    motivation_header = [['Name', 'Category', 'Description']]

    # File header list
    header_list = [enemy_header, location_header, quest_item_header, motivation_header]







    # Add record prompts
    enemy_add_name_prompt = 'Enter a new name: '
    enemy_add_type_prompt = 'Enter the type: '
    location_add_name_prompt = 'Enter a new name: '
    location_add_sol_sys_prompt = 'Enter the solar system: '
    location_add_gal_loc_prompt = 'Enter the galactic location: '
    location_add_loc_type_prompt = 'Enter location type: '
    quest_item_add_name_prompt = 'Enter a new name: '
    quest_item_add_type_prompt = 'Enter the type: '
    quest_item_add_effect_prompt = 'Enter quest item effect: '   
    motivation_add_name_prompt = 'Enter a new name: '
    motivation_add_category_prompt = 'Enter the category: '
    motivation_add_description_prompt = 'Enter the description: '

    # Add record list made from add record prompts
    add_rec_prompt_list = [enemy_add_name_prompt, enemy_add_type_prompt,  location_add_name_prompt,
                           location_add_sol_sys_prompt, location_add_gal_loc_prompt,
                           location_add_loc_type_prompt, quest_item_add_name_prompt,
                           quest_item_add_type_prompt, quest_item_add_effect_prompt,
                           motivation_add_name_prompt, motivation_add_category_prompt,
                           motivation_add_description_prompt]


    

    # Name Prompts for edit file functions
    edit_minion_name = 'Name of Minion you want to change: '
    edit_rival_name = 'Name of Rival you want to change: '
    edit_nemesis_name = 'Name of Nemesis you want to change: '
    edit_location_name = 'Name of the Location you wish to change?: '
    edit_quest_item_name = 'Name of the Quest Item you want to change: '
    edit_motivation_name = 'Name of the Motivation you want to change: '

    # Name prompts list for edit file
    edit_records_list_name = [edit_minion_name, edit_rival_name, edit_nemesis_name,
                         edit_location_name, edit_quest_item_name,
                         edit_motivation_name]



    # Type and category prompts for edit file functions
    new_enemy_type = 'Enter new Enemy type: '
    new_system = 'Enter new Solar System: '
    new_gal_loc = 'Enter new Galactic location: '
    new_loc_type = 'Enter new location type: '
    new_quest_item_type = 'Enter new Quest Item type: '
    new_quest_item_effect = 'Enter new Quest Item effect: '
    new_motivation_category = 'Enter new Motivation Category: '
    new_motivation_description = 'Enter new Motivation Description: '

    # Type and category prompts for edit file functions list
    edit_type_prompts = [new_enemy_type, new_system, new_gal_loc, new_loc_type, new_quest_item_type,
                         new_quest_item_effect, new_motivation_category, new_motivation_description]





    # Edit record yes and no prompts
    edit_enemy_type_prompt = 'Do you want to change the enemy Type?(y or n): '
    edit_system_prompt = 'Do you want to Change the Solar System field?(y or n): '
    edit_gal_loc_prompt = 'Do you want to change the Galactic Location field?(y or n): '
    edit_loc_type_prompt = 'Do you want to change the Location Type field?(y or n): '
    edit_quest_item_type_prompt = 'Do you want to change the Quest Item type?(y or n): '
    edit_quest_item_effect_prompt = 'Do you want to change the Quest Item Effect?(y or n): '
    edit_motivation_category_prompt = 'Do you want to change the Motivation Category?(y or n): '
    edit_motivation_description_prompt = 'Do you want to change the Motivation Description?(y or n): '

    # Edit record yes and no prompts list
    edit_record_prompt_list = [edit_enemy_type_prompt, edit_system_prompt, edit_gal_loc_prompt,
                               edit_loc_type_prompt, edit_quest_item_type_prompt,
                               edit_quest_item_effect_prompt, edit_motivation_category_prompt,
                               edit_motivation_description_prompt]





    # adventure creator prompts
    min_prompt = 'Enter the amount of Minions you want in the adventure: '
    riv_prompt = 'Enter the amount of Rivals you want in the adventure: '
    enter_a_number = 'Please enter a whole number'
    file_prompt = 'What name do you want to use as a file name: '
    min_message = 'Minion: '
    riv_message = 'Rival: '
    nem_message = 'Nemesis: '
    loc_message = 'Location: '
    q_i_message = 'Quest Item: '
    mot_message = 'Motive: '

    # adventure creator prompts list
    adv_cr_list = [min_prompt, riv_prompt, enter_a_number, file_prompt, min_message,
                   riv_message, nem_message, loc_message, q_i_message, mot_message]

    


    
    # Main Menu choices
    add_to_file = '1) Add a record to an existing file'
    edit_record_in_file = '2) Edit an existing record in a file'
    delete_record = '3) Delete a record from an existing file'
    create_adventure_file = '4) create an adventure file'
    quit_program = '5) quit program'

    # Main Menu choices list
    main_menu_choices = [add_to_file, edit_record_in_file,
                         delete_record, create_adventure_file, quit_program]


    # Add record to a file menu choices
    add_to_minion_record = '1) Add a record to the Minion file'
    add_to_rival_record = '2) Add a record to the Rival file'
    add_to_nemeses_record = '3) Add a record to the Nemesis file'
    add_to_location_record = '4) Add a record to the Location file'
    add_to_quest_item_record = '5) Add a record to the Quest Item file'
    add_to_motivation_record = '6) Add a record to the Motitvation file'
    add_to_return = '7) Return to main menu'

    # Add record to a file menu choices list
    add_record_list = [add_to_minion_record, add_to_rival_record, add_to_nemeses_record,
                       add_to_location_record, add_to_quest_item_record,
                       add_to_motivation_record, add_to_return]

                         
    # Edit a record in a file menu choices
    edit_minion_record = '1) Edit Minion record'
    edit_rival_record = '2) Edit Rival record'
    edit_nemesis_record = '3) Edit Nemesis record'
    edit_location_record = '4) Edit location record'
    edit_quest_item_record = '5) Edit Quest Item record'
    edit_motivation_record = '6) Edit Motivation record'
    edit_return = '7) Return to main menu'

    # Edit record menu choices list
    edit_menu_choices = [edit_minion_record, edit_rival_record, edit_nemesis_record,
                         edit_location_record, edit_quest_item_record,
                         edit_motivation_record, edit_return]
                         


    # Deactivate record menu choices
    deactivate_minion_record = '1) Deactivate a record from the Minion file'
    deactivate_rival_record = '2) Deactivate a record from the Rival file'
    deactivate_nemesis_record = '3) Deactivate a record from the Nemesis file'
    deactivate_location_record = '4) Deactivate a record from the Location file'
    deactivate_quest_item_record = '5) Deactivate a record from the Quest Item file'
    deactivate_motivation_record = '6) Deactivate a record from the Motivation file'
    
    deactivate_return = '7) Return to main menu'

    # Deactivate record menu choices list
    deactivate_menu_list = [deactivate_minion_record, deactivate_rival_record,
                            deactivate_nemesis_record, deactivate_location_record,
                            deactivate_quest_item_record, deactivate_motivation_record,
                            deactivate_return]
    


    # Adventure Creator menu choices
    adv_create = '1) Create new Adventure'
    adv_return = '2) Return to main menu'

    # Adventure Creator menu choices list
    adv_cr_menu = [adv_create, adv_return]


                          
    # messages if there are no files found
    no_minions_file = 'Creating Minions file...'
    no_rivals_file = 'Creating Rivals file...'
    no_nemeses_file = 'Creating Nemeses file...'
    no_locations_file = 'Creating locations file...'
    no_quest_items_file = 'Creating Quest Items file...'
    no_motivations_file = 'Creating Motivations file...'

    # List of messages if there are no files found
    no_file_list = [no_minions_file, no_rivals_file, no_nemeses_file, no_locations_file,
                    no_quest_items_file, no_motivations_file]


    
    print(title, '\n', subtitle, sep ='')
    print(program_description)
    input(enter_to_continue)

    menu_done = False
    while menu_done == False:

        # create lists from .csv files, and creates new files if
        # there are no files already created
        minions = get_lists.get_min_list(no_file_list, file_name_list)
        rivals = get_lists.get_riv_list(no_file_list, file_name_list)
        nemeses = get_lists.get_nem_list(no_file_list, file_name_list)
        locations = get_lists.get_loc_list(no_file_list, file_name_list)
        quest_items = get_lists.get_q_i_list(no_file_list, file_name_list)
        motivations = get_lists.get_mot_list(no_file_list, file_name_list)

        #create master list of lists that are created from the csv files
        master_list = [minions, rivals, nemeses, locations, quest_items, motivations]

        # Prints the main menu as 5 individual choices
        menu.print_main_menu(main_menu_choices)

        # Input for making the menu choice
        token = input('\n' + menu_prompt)

        # Choice 1 that lets the user add a new record to a file
        if token == '1':
            menu.add_record_to_file(master_list, add_record_list, add_rec_prompt_list,
                                    add_again_prompt, file_name_list, header_list,
                                    need_name, menu_prompt, title_list,
                                    enter_choice)

        # Choice 2 that lets the user edit a record in a file
        elif token == '2':
            menu.edit_file(master_list, edit_menu_choices, edit_records_list_name,
                           edit_type_prompts, header_list, edit_record_prompt_list,
                           file_name_list, not_found, menu_prompt, title_list,
                           enter_choice)

        # Choice 3 that lets the user deactivate a record into a dump
        # file
        elif token == '3':
            menu.deactivate_records(master_list, deactivate_menu_list, header_list,
                                    file_name_list, dump_file_list, deactivate_record_prompt,
                                    del_again_prompt, not_found, menu_prompt, title_list,
                                    enter_choice)

        # Choice 4 that lets the user createan adventure and define a name for
        # for a new adventure file
        elif token == '4':
            menu.create_adventure(master_list, adv_cr_list, adv_cr_menu, menu_prompt,
                                  must_have_file, enter_choice)

        # Choice 5 that lets the user end the program
        elif token == '5':
            menu_done = True

        # If the user doesnt make a choice from 1 through 5
        else:
            print(enter_choice)

main()

        

