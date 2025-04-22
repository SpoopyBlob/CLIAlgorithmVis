import os
import time
import random
import visual as v

auto_type = 0
auto_speed = 1.5

def system_clear():
    os.system("cls" if os.name == "nt" else "clear")

def random_list_generator(list_size = 10):
    random_list = []
    for i in range(list_size):
        random_list.append(random.randint(1, 100))

    return random_list, random_list[random.randint(0, list_size - 1)]

def random_list_generator_sort(list_size = 5):
    random_list = []
    for i in range(list_size):
        random_list.append(random.randint(1, 100))

    return random_list

def auto_manual(type = 0):
    #auto
    if type == 0:
         time.sleep(auto_speed)   
    else:
        input("Type any character to continue: ")

def colour_change(user_input):
    if user_input.lower() == "e":
        return True
    
    parts = user_input.split()

    if len(parts) == 3 and all(p.isdigit() for p in parts):
        v.colour_legend['match'] = v.colour[parts[0]]
        v.colour_legend['none_match'] = v.colour[parts[1]]
        v.colour_legend['default'] = v.colour[parts[2]]

        print(f"\033[{v.colour_legend['default']}mChange successful!\033[0m")
        time.sleep(1)
        return True
    else:
        print(f"\033[{v.colour_legend['none_match']}mInvalid input!\033[0m Please enter three digits seperated by spaces.")
        time.sleep(1)
        return False
    


