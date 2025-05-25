import visual as v
import utilities as u
import navigate_feature as n
import input_handling as i

def naive_pattern_search(string, pattern):
    match_count = 0

    for idx in range(len(string) - len(pattern) + 1):
        
        nps_step_one(string, pattern, idx, match_count)
        n.Transfer.push_to_node()
        
        for idx_2 in range(len(pattern)):
            result = False

            if string[idx + idx_2] == pattern[idx_2]:
                match_count += 1
                result = True
                
            nps_step_two(string, pattern, idx, idx_2, match_count, result)
            n.Transfer.push_to_node()

            if result == False:
                break

            if match_count == len(pattern):
                nps_step_match(string, pattern, idx, idx_2, match_count)
                n.Transfer.push_to_node()
                return
            
    nps_step_none_match(string, pattern)
    n.Transfer.push_to_node()

def nps_step_one(string, pattern, idx, match_count):
    u.system_clear()
    v.two_step_views(string, pattern, idx, idx, highlight_2 = False)
    v.format_string("Match_count = ", f"{match_count}")
    v.format_string("Accessing outer loop index ", idx)
    u.auto_manual()

def nps_step_two(string, pattern, idx, idx_2, match_count, result):
    u.system_clear()
    v.two_step_views(string, pattern, idx + idx_2, idx_2)
    v.format_string("Match_count = ", f"{match_count}")
    v.compare_search(string, idx + idx_2, pattern[idx_2], result)
    u.auto_manual()

def nps_step_match(string, pattern, idx, idx_2, match_count):
    u.system_clear()
    v.two_step_views(string, pattern, idx + idx_2, idx_2)
    v.format_string("Match_count is equal to length of pattern: ", f"{match_count}")
    v.format_string("Pattern starts at index ", f"{idx}")
    u.auto_manual(mod = 1)

def nps_step_none_match(string, pattern):
    u.system_clear()
    v.two_step_views(string, pattern, 0, 0, highlight_1 = False, highlight_2 = False)
    v.none_match_message("\nPattern not found!")
    u.auto_manual(mod = 1)
    

#linear search ------------------------------------------------------------------------------------------
def linear_search(lst, target):
    for idx in range(len(lst)):
        ls_step_one(lst, idx, target)
        n.Transfer.push_to_node()

        result = False
        
        if lst[idx] == target:
            result = True


        ls_step_two(lst, idx, target, result)
        n.Transfer.push_to_node()

        if result == True:
            return
        

    ls_final_step()
    n.Transfer.push_to_node()
    u.auto_manual(mod = 1)
    return

def ls_step_one(lst, idx, target):
    u.system_clear()
    v.step_view(lst, idx, target)
    v.format_string("Accessing index", idx)
    v.format_string("Searching for target:", target, newline=False)
    u.auto_manual()

def ls_step_two(lst, idx, target, result):
    u.system_clear()
    v.step_view(lst, idx, target)
    v.compare_search(lst, idx, target, result)
    u.auto_manual()

def ls_final_step():
    u.system_clear()
    v.none_match_message("No matches!")
    u.auto_manual()

#bubble sort --------------------------------------------------------------------------------------------
def bubble_sort(arr):
    for i in range(len(arr)):
        for index in range(len(arr) - i - 1):
            result = False

            if arr[index] > arr[index + 1]:
                result = True
                bs_step_one(arr, i, index, result)
                temp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = temp
            else:
                bs_step_one(arr, i, index, result)
                
    bs_step_final(arr)

def bs_step_one(arr, i, index, result):
    u.system_clear()
    v.two_step_views(arr, arr, index, index + 1, "List", "Comparision")
    u.auto_manual()
    v.compare_sort(arr, index, index + 1, result)
    n.Transfer.push_to_node()

def bs_step_final(arr):
    u.system_clear()
    v.format_string("New sorted list:", arr)
    n.Transfer.push_to_node()
    u.auto_manual()

#merge sort ---------------------------------------------------------------------------------
def merge_sort_helper(item1, item2):

    result = []

    while item1 and item2:
        if item1[0] > item2[0]:
            result.append(item2[0])
            item2.pop(0)
        elif item1[0] < item2[0]:
            result.append(item1[0])
            item1.pop(0)
        else:
            result.append(item1[0])
            item1.pop(0)

    if item1:
        result += item1
    elif item2:
        result += item2
    
    return result

def merge_sort(items, indent = 0):

    if indent == 0:
        ms_split(0, "call", f"First function call: {items}")
 

    #base case
    if len(items) <= 1:
        ms_split(indent + 1, "call", f"Base case reached: {items}")
        return items
    
    #slicing
    middle_index = len(items) // 2
    right_side = items[middle_index:]
    left_side = items[:middle_index]

    #recursion
    ms_split(indent + 1, "call", f"Left split: {items[:middle_index]}")
    left_sorted = merge_sort(left_side, indent + 1)


    ms_split(indent + 1, "call", f"Right split: {items[middle_index:]}")
    right_sorted = merge_sort(right_side, indent + 1)
 

    ms_split(indent + 1, "return", f"Merging results: {items}")
    result = merge_sort_helper(right_sorted, left_sorted)
    ms_split(indent + 1, "return", f"Sorted: {result}")


    if indent == 0:
        ms_split(0, "return", f"Final merge: {result}")
        
    return result

def ms_split(indent, type, str):
    v.recursive_visual(indent, type, str)
    n.Transfer.rec_push_to_node()
    u.auto_manual()
    
