import os
import time
import random
auto_speed = 1
auto_type = 0
color_legend = {"match": "34", "none_match": "31", "default": "33"}

#todo
    #Setting function
        #step by step mode/auto
        #colour legend 
        #speed of auto

#user control --------------------------------------------------------------------
def user_control():
    valid_input = False
    while not valid_input:
        os.system("clear")
        print(f"\033[{color_legend["default"]};1;4mCLI Algorithm Visualizer\033[0m")

        print(f"""
\033[{color_legend["default"]}m[0] \033[0mLinear Search
\033[{color_legend["default"]}m[1] \033[0mNaive Pattern Search
\033[{color_legend["default"]}m[2] \033[0mSettings
\033[{color_legend["default"]}m[3] \033[0mExit
          """)
        
        user_input = input("Enter input here: ")

        if user_input == "0":
            list_size = input("Enter list size: ")
            try:
                list, target = random_list_generator(list_size = int(list_size))
            except ValueError:
                print(f"Invalid format, try again")
                time.sleep(1)
                continue

            #Need to display target within txt
            print(linear_search(list, target))
            time.sleep(1)

        elif user_input == "1":
            string = input("Enter string: ")
            target = input("Enter target: ")
            
            naive_pattern_search(string, target)

        elif user_input == "2":
            settings()
        elif user_input == "3":
            valid_input = True
            break

        else:
            print("Invalid input, try again!")

def settings():
    print(f"""
\033[{color_legend["default"]}m[0] \033[0mAuto/Manual Mode
\033[{color_legend["default"]}m[1] \033[0mAuto Speed
\033[{color_legend["default"]}m[2] \033[0mColor Legend
\033[{color_legend["default"]}m[3] \033[0mExit
    """)

    user_input = input("Enter here: ")

    if user_input == "0":
        print(f"""
\033[{color_legend["default"]}m[0] \033[0mAuto Mode
\033[{color_legend["default"]}m[1] \033[0mManual Mode
\033[{color_legend["default"]}m[2] \033[0mExit
        """)
        user_input_2 = input("Enter here: ")
        global auto_type

        if user_input_2 == "0":
            auto_type = 0
        elif user_input_2 == "1":
            auto_type = 1
        else:
            return
        
    if user_input == "1":
        speed = input("Enter auto speed in seconds: ")
        global auto_speed 
        try:
            speed = int(speed)
        except ValueError:
            print("Error, you can only use integars as an input.")
            time.sleep(2)
        auto_speed = speed

    if user_input == "2":
        color_leg()

    else:
        return

#utility --------------------------------------------------------------------------------
def random_list_generator(list_size = 10):
    random_list = []
    for i in range(list_size):
        random_list.append(random.randint(1, 100))

    return random_list, random_list[random.randint(0, list_size - 1)]

def auto_manual(type = 0):
    #auto
    if type == 0:
         time.sleep(auto_speed)   
    else:
        input("Type any character to continue: ")

def color_leg():
    global color_legend
    colors = {
    "0": "30", #black
    "1": "31", #red
    "2": "32", #green
    "3": "33", #yellow
    "4": "34", #blue
    "5": "35", #magenta
    "6": "36", #cyan
    "7": "37"} #white

    print(f"""
\033[1;4mColors\033[0m
\033[{colors["0"]}m[0] \033[0m Black
\033[{colors["1"]}m[1] \033[0m Red
\033[{colors["2"]}m[2] \033[0m Green
\033[{colors["3"]}m[3] \033[0m Yellow
\033[{colors["4"]}m[4] \033[0m Blue
\033[{colors["5"]}m[5] \033[0m Magenta
\033[{colors["6"]}m[6] \033[0m Cyan
\033[{colors["7"]}m[7] \033[0m White
      
\033[1;4mCurrrent setup\033[0m
\033[{color_legend["match"]}m[0] \033[0m Match
\033[{color_legend["none_match"]}m[1] \033[0m None match
\033[{color_legend["default"]}m[2] \033[0m Default        

\033[{color_legend["default"]}m[E] \033[0m Exit setup      

To change your color legend, select the number of the colors you would like to change in the order of the \033[1;4mCurrrent setup\033[0m.

e.g. 1 2 3 ---> match color = red, none match = green & default = yellow
    """)

    user_input = input("")

    if user_input.lower() == "e":
        return
    
    split_user_input = user_input.split()
    try:
        match = colors[split_user_input[0]]
        none_match = colors[split_user_input[1]]
        default = colors[split_user_input[2]]

        color_legend["match"] = match
        color_legend["none_match"] = none_match
        color_legend["default"] = default

    except KeyError:
        print("Error: Either the formating or name was wrong, returning to home screen")
        time.sleep(2.5)


#Algorithms--------------------------------------------------------------------------
def naive_pattern_search(string, pattern):

    for idx in range(len(string) - len(pattern) + 1):
        match_count = 0

        two_step(string, pattern, idx, idx, highlight_2 = False )
        format_string("Match_count = ", f"{match_count}")
        format_string("Accessing outer loop index ", idx)
        auto_manual(auto_type)
        
        for idx_2 in range(len(pattern)):
            
            two_step(string, pattern, idx + idx_2, idx_2)
            format_string("Match_count = ", f"{match_count}")
            if compare(string, idx + idx_2, pattern[idx_2], "String"):
                match_count += 1
            else:
                break
            
            if match_count == len(pattern):
                two_step(string, pattern, idx + idx_2, idx_2)
                format_string("Match_count is equal to length of pattern: ", f"{match_count}")
                format_string("Pattern starts at index ", f"{idx}")
                auto_manual(auto_type)
                return

#linear search
def linear_search(lst, target):
    for idx in range(len(lst)):
        one_step(lst, idx, target)
        format_string("Accessing index", idx)
        format_string("Searching for target:", target, newline=False)
        auto_manual(auto_type)
        
        one_step(lst, idx, target)
        if compare(lst, idx, target):
            os.system("clear")
            return f"\033[{color_legend["match"]}mMatch Found\033[0m at index {idx}"
        
    os.system("clear")
    return f"\033[{color_legend["none_match"]}mTarget item not found"
#Visual ---------------------------------------------------------------------------------------
#Compare elements
def compare(item, idx, target, item_type = "List"):
    
    print(f"\n\nComparing \033[{color_legend["default"]}m{item[idx]}\033[0m with target {target}...")
    auto_manual(auto_type)
    
    if item[idx] == target:
        print(f"\033[{color_legend["match"]}mMatch Found!\033[0m")
        auto_manual(auto_type)
        return True
    else:
        print(f"\033[{color_legend["none_match"]}mDoes Not Match!\033[0m")
        auto_manual(auto_type)
        return False
    
#highlights the current iteration
def highlight(item, highlight_idx, highlight = True):

    if highlight == False:
        return " ".join(map(str, item))
    
    #Note for self: map will convert each item into a string without any formating
    left_side = " ".join(map(str, item[:highlight_idx]))
    highlight = str(item[highlight_idx]).strip("[]")
    right_side = " ".join(map(str, item[highlight_idx + 1:]))

    text = f"{left_side} \033[{color_legend["default"]}m{highlight} \033[0m{right_side}"

    return text

#access index (1 item)
def one_step(item, idx, target, item_type = "List"):
    os.system("clear")
    print(f"\033[1;4m{item_type}:\033[0m " + highlight(item, idx))
    format_string("Target:", target, newline = False, code = "1;4m")
#access index (2 item)
def two_step(item_1, item_2, idx_1, idx_2, item_type = "String", highlight_2 = True):
    os.system("clear")
    print(f"\033[1;4m{item_type}:\033[0m " + highlight(item_1, idx_1))
    print(f"\033[1;4mTarget {item_type}:\033[0m " + highlight(item_2, idx_2, highlight = highlight_2))
#format string 
def format_string(msg, var, newline = True, code = ""):
    if newline:
        new = "\n\n"
    else:
        new = ""

    if code != "":
        code = "\033[" + code

    print(f"{code}{new}{msg}\033[0m \033[{color_legend["default"]}m{var} \033[0m")

#main--------------------------------------------------------------------------

user_control()
#os.system("clear")
