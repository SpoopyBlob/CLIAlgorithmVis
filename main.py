import utilities as u
import visual as v
import input_handling as i

def user_control():
    while True:
        v.main_print()

        user_input = input("Enter input here: ")

        if user_input == "0":
            i.linear_search_setup()

        elif user_input == "1":
            i.naive_pattern_search_setup()

        elif user_input == "2":
            i.bubble_sort_setup()

        elif user_input == "3":
            i.merge_sort_setup()

        elif user_input == "4":
            settings()

        elif user_input == "5":
            break

        else:
            v.error_message("Invalid Input")
            u.auto_manual()

def settings():
    while True:
        v.settings_main_print()

        user_input = input("Enter here: ")

        #Auto/Manual Mode
        if user_input == "0":
            i.auto_manual_mode()
                    
        #auto speed
        elif user_input == "1":
            i.auto_speed()
        
        elif user_input == "2":
            i.colour_legend_setup()
        
        elif user_input == "3":
            return
        
        else:
            v.error_message("Invalid Input")
            u.auto_manual()

user_control()