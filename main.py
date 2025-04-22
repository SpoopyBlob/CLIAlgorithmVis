import utilities as u
import algorithm as a
import visual as v
import time

#address error handling, make it consistant
#address time.sleep system
#

def user_control():
    while True:
        v.main_print()

        user_input = input("Enter input here: ")

        if user_input == "0":
            list_size = input("Enter list size: ")
            if not list_size.isdigit():
                print("Please enter a valid number. ")
                time.sleep(1)
                continue
            
            try:
                list, target = u.random_list_generator(list_size = int(list_size))
            except ValueError:
                print(f"Invalid format, try again")
                time.sleep(1)
                continue

            print(a.linear_search(list, target))
            time.sleep(1)

        elif user_input == "1":
            string = input("Enter string: ")
            target = input("Enter target: ")
            
            a.naive_pattern_search(string, target)

        elif user_input == "2":
            list_size = input("Enter list size: ")
            if not list_size.isdigit():
                print("Please enter a valid number. ")
                time.sleep(1)
                continue
            
            a.bubble_sort(u.random_list_generator_sort(int(list_size)))

        elif user_input == "3":
            list_size = input("Enter list size: ")
            if not list_size.isdigit():
                print("Please enter a valid number. ")
                time.sleep(1)
                continue

            a.merge_sort(u.random_list_generator_sort(int(list_size)))

        elif user_input == "4":
            settings()
        elif user_input == "5":
            break
        else:
            print("Invalid input, try again!")
            time.sleep(1)

def settings():
    while True:
        v.settings_main_print()

        user_input = input("Enter here: ")

        #Auto/Manual Mode
        if user_input == "0":
            v.auto_manual_print()

            user_input_2 = input("Enter here: ")

            if user_input_2 == "0":
                u.auto_type = 0 #auto
            elif user_input_2 == "1":
                u.auto_type = 1 #manual
            else:
                return 
        #auto speed
        elif user_input == "1":
            speed = input("Enter auto speed in seconds: ")
            try:
                speed = int(speed)
                u.auto_speed = speed
            except ValueError:
                print("Error, you can only use integars as an input.")
                time.sleep(2)
        
        elif user_input == "2":
            valid_input = False
            while not valid_input:
                v.colour_legend_print()
                user_input = input("Enter here: ")
                valid_input = u.colour_change(user_input)
        
        elif user_input == "3":
            return
        
        else:
            print("Error: Invalid input")
            time.sleep(1)

user_control()