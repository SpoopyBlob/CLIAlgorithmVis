import os
import time

#before naive pattern search, try to modulize your functions even further

def pattern_search(string, pattern):

    for idx in range(len(string)):
        match_count = 0
        
        for char in range(len(pattern)):
            if string[idx + char] == pattern[char]:
                match_count += 1
            else:
                break
            
            if match_count == len(pattern):
                print(f"{pattern} found at index {idx}")
                return

#linear search
def linear_search(list, target):
    for idx in range(len(list)):
        print("\033[1;4mList:\033[0m " + highlight(list, idx))
        print(f"\n\nAccessing index \033[33m{idx} \033[0m")
        time.sleep(1)

        if compare(list[idx], target, list, idx):
            os.system("clear")
            return f"\033[34mMatch Found\033[0m at index {idx}"
        
    os.system("clear")
    return "\033[31mTarget item not found"

#compare elements
def compare(item, target, object, idx):
    print("\033[1;4mList:\033[0m " + highlight(object, idx))
    print(f"\n\nComparing \033[33m{item}\033[0m with target {target}...")
    time.sleep(1)
    if item == target:
        print("\033[34mMatch Found!\033[0m")
        time.sleep(1)
        return True
    else:
        print("\033[31mDoes Not Match!\033[0m")
        time.sleep(1)
        return False
    
#highlights the current iteration
def highlight(object, highlight_idx):

    os.system("clear")

    #Note for self: map will convert each item into a string without any formating
    left_side = " ".join(map(str, object[:highlight_idx]))
    highlight = str(object[highlight_idx]).strip("[]")
    right_side = " ".join(map(str, object[highlight_idx + 1:]))

    text = f"{left_side} \033[33m{highlight} \033[0m{right_side}"

    return text

os.system("clear")
print(linear_search([23, 65, 34, 23, 34, 43], 343))
