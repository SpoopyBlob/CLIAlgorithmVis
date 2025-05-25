import os
import time
import random
import visual as v

auto_type = 0
auto_speed = 1.5

def system_clear():
    os.system("cls" if os.name == "nt" else "clear")

def random_list_generator_target(list_size = 10):
    random_list = []
    
    for i in range(list_size):
        random_list.append(random.randint(1, 100))

    return random_list, random_list[random.randint(0, list_size - 1)]

def random_list_generator(list_size = 5):
    random_list = []

    for i in range(list_size):
        random_list.append(random.randint(1, 100))

    return random_list

def auto_manual(mod = None):
    global auto_type
    #auto
    if auto_type == 0:
         time.sleep(auto_speed + mod if mod is not None else auto_speed)   
    #manual
    else:
        input("Enter any character to continue: ")

def colour_change(parts):

    v.colour_legend['match'] = v.COLOUR[parts[0]]
    v.colour_legend['none_match'] = v.COLOUR[parts[1]]
    v.colour_legend['default'] = v.COLOUR[parts[2]]

    print(f"\033[{v.colour_legend['default']}mChange successful!\033[0m")
    auto_manual()