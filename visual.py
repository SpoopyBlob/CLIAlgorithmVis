import utilities as u
import navigate_feature as n
COLOUR = {
    0: "30", #black
    1: "31", #red
    2: "32", #green
    3: "33", #yellow
    4: "34", #blue
    5: "35", #magenta
    6: "36", #cyan
    7: "37"  #white
    } 

colour_legend = {"match": "34", "none_match": "31", "default": "33"}

def error_message(msg):
    print(f"\n\033[{colour_legend['none_match']}mERROR:\033[0m {msg}")

def none_match_message(msg):
    txt = f"\033[{colour_legend['none_match']}m{msg}\033[0m"
    n.Transfer.update_txt(txt + "\n")
    print(txt)

def system_message(msg):
    print(f"\033[{colour_legend['match']}m{msg}\033[0m")

def format_string(msg, var, newline = True, code = ""):
    if newline:
        new = "\n\n"
    else:
        new = ""

    if code != "":
        code = "\033[" + code

    txt = f"{code}{new}{msg}\033[0m \033[{colour_legend['default']}m{var}\033[0m"
    n.Transfer.update_txt(txt + "\n")
    print(txt)

#highlights the item in a list that is current being checked
def highlight(item, highlight_idx, highlight = True):

    colour = colour_legend['default']
        
    left_side = " ".join(map(str, item[:highlight_idx]))
    highlight = str(item[highlight_idx]).strip("[]")
    right_side = " ".join(map(str, item[highlight_idx + 1:]))

    text = f"{left_side} \033[{colour}m{highlight} \033[0m{right_side}"

    return text

def step_view(item, idx, target, item_type = "List"):
    txt = f"\033[1;4m{item_type}:\033[0m " + highlight(item, idx)
    n.Transfer.update_txt(txt + "\n")
    print(txt)
    format_string("Target:", target, newline = False, code = "1;4m")


def two_step_views(item_1, item_2, idx_1, idx_2, item_type = "String", item_type_2 = "Target", highlight_1 = True, highlight_2 = True):
    txt = f"\033[1;4m{item_type}:\033[0m " + highlight(item_1, idx_1, highlight_1)
    txt_2 = f"\033[1;4m{item_type_2} {item_type}:\033[0m " + highlight(item_2, idx_2, highlight = highlight_2)
    n.Transfer.update_txt(txt + " " + txt_2 + "\n")
    print(txt, txt_2)
    
    
def compare_search(item, idx, target, result):
    
    txt = f"\n\nComparing \033[{colour_legend['default']}m{item[idx]}\033[0m with target {target}..."
    print(txt)
    u.auto_manual()
    
    if result == True:
        txt_2 = f"\033[{colour_legend['match']}mMatch Found at index {idx}!\033[0m"
        n.Transfer.update_txt(txt + "\n" + txt_2 +"\n")        
        print(txt_2)


    else:
        txt_2 = f"\033[{colour_legend['none_match']}mDoes Not Match!\033[0m"
        n.Transfer.update_txt(txt + "\n" + txt_2 + "\n")
        print(txt_2)


    
def compare_sort(item, idx, idx_2, result):
    txt = f"\n\nComparing \033[{colour_legend['default']}m{item[idx]}\033[0m with\033[{colour_legend['default']}m {item[idx_2]} \033[0m\n"
    print(txt)

    u.auto_manual()

    if result == True:
        txt_2 = f"\033[{colour_legend['match']}m{item[idx]} > {item[idx_2]}!\033[0m\nSwapping values!\n"
        n.Transfer.update_txt(txt + txt_2)
        print(txt_2)
        u.auto_manual()
        return True
    
    else:
        txt_2 = f"\033[{colour_legend['none_match']}m{item[idx]} < {item[idx_2]}!\033[0m\nNo swap needed!\n"
        n.Transfer.update_txt(txt + txt_2)
        print(txt_2)
        u.auto_manual()
        return False

def recursive_visual(indent, call_return, msg):
    #colour
    rec_colour = "\033[" + colour_legend["match" if call_return == "call" else "none_match"] + "m"
    reset = "\033[0m"
    #format
    symbol = "├──[Call]" if call_return == "call" else "└──[Return]"
    txt = "" if indent == 0 else rec_colour + ("│  " * indent)

    if indent > 0:
        txt += f"{rec_colour}{symbol}{reset}{msg}\n"
    else:
        txt += f"{rec_colour}{symbol[3:]}{reset}{msg}\n"
    
    n.Transfer.update_txt(txt + "\n")
    print(txt)



#Print to screen blocks --------------------------------------------------------------------------------------------------

def colour_legend_print():
    u.system_clear()
    print(f"""
\033[1;4mColors\033[0m
\033[{COLOUR[0]}m[0] \033[0m Black
\033[{COLOUR[1]}m[1] \033[0m Red
\033[{COLOUR[2]}m[2] \033[0m Green
\033[{COLOUR[3]}m[3] \033[0m Yellow
\033[{COLOUR[4]}m[4] \033[0m Blue
\033[{COLOUR[5]}m[5] \033[0m Magenta
\033[{COLOUR[6]}m[6] \033[0m Cyan
\033[{COLOUR[7]}m[7] \033[0m White
      
\033[1;4mCurrent setup\033[0m
\033[{colour_legend['match']}m[0] \033[0m Match
\033[{colour_legend['none_match']}m[1] \033[0m None match
\033[{colour_legend['default']}m[2] \033[0m Default        

\033[{colour_legend['default']}m[E] \033[0m Exit setup      

To change your colour legend, use the corrosponding colours above with the correct format, example below

e.g. 1 2 3 ---> match color = red, none match = green & default = yellow
    """)

def main_print():
    u.system_clear()
    print(f"\033[{colour_legend['default']};1;4mCLI Algorithm Visualizer\033[0m")

    print(f"""
\033[{colour_legend['default']}m[0] \033[0mLinear Search
\033[{colour_legend['default']}m[1] \033[0mNaive Pattern Search
\033[{colour_legend['default']}m[2] \033[0mBubble Sort
\033[{colour_legend['default']}m[3] \033[0mMerge Sortt
\033[{colour_legend['default']}m[4] \033[0mSettings
\033[{colour_legend['default']}m[5] \033[0mExit
    """)

def settings_main_print():
    u.system_clear()
    print(f"""
\033[{colour_legend['default']}m[0] \033[0mAuto/Manual Mode
\033[{colour_legend['default']}m[1] \033[0mAuto Speed
\033[{colour_legend['default']}m[2] \033[0mColor Legend
\033[{colour_legend['default']}m[3] \033[0mExit
    """)

def auto_manual_print():
    u.system_clear()
    print(f"""
\033[{colour_legend['default']}m[0] \033[0mAuto Mode
\033[{colour_legend['default']}m[1] \033[0mManual Mode
\033[{colour_legend['default']}m[2] \033[0mExit
    """)

def navigate_print():
    print(f"""
\033[{colour_legend['default']}m[0] \033[0mBackwards \033[{colour_legend['default']}m[1] \033[0mForwards \033[{colour_legend['default']}m[E] \033[0mExit
    """)