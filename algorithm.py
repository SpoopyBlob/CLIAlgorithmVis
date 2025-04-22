import visual as v
import utilities as u

def naive_pattern_search(string, pattern):

    for idx in range(len(string) - len(pattern) + 1):
        match_count = 0

        v.two_step(string, pattern, idx, idx, highlight_2 = False )
        v.format_string("Match_count = ", f"{match_count}")
        v.format_string("Accessing outer loop index ", idx)
        u.auto_manual(u.auto_type)
        
        for idx_2 in range(len(pattern)):
            
            v.two_step(string, pattern, idx + idx_2, idx_2)
            v.format_string("Match_count = ", f"{match_count}")
            if v.compare_search(string, idx + idx_2, pattern[idx_2], "String"):
                match_count += 1
            else:
                break
            
            if match_count == len(pattern):
                v.two_step(string, pattern, idx + idx_2, idx_2)
                v.format_string("Match_count is equal to length of pattern: ", f"{match_count}")
                v.format_string("Pattern starts at index ", f"{idx}")
                u.auto_manual(u.auto_type)
                return
            
    print(f"\033[{v.colour_legend['none_match']}mTarget pattern not found")
    u.auto_manual(u.auto_type)

#linear search
def linear_search(lst, target):
    for idx in range(len(lst)):
        v.one_step(lst, idx, target)
        v.format_string("Accessing index", idx)
        v.format_string("Searching for target:", target, newline=False)
        u.auto_manual(u.auto_type)
        
        v.one_step(lst, idx, target)
        if v.compare_search(lst, idx, target):
            u.system_clear()
            return f"\033[{v.colour_legend['match']}mMatch Found\033[0m at index {idx}"
        
    u.system_clear()
    return f"\033[{v.colour_legend['none_match']}mTarget item not found"

def bubble_sort(arr):
    for i in range(len(arr)):
        for index in range(len(arr) - i - 1):
            v.two_step(arr, arr, i, index, "List")
            u.auto_manual()

            if v.compare_sort(arr, index, index + 1):
                temp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = temp

    v.format_string("New sorted list:", arr)

#merge sort helper function , merge
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
        v.recursive_visual(0, "call", f"First function call: {items}")
        u.auto_manual(u.auto_type)

    #base case
    if len(items) <= 1:
        v.recursive_visual(indent + 1, "call", f"Base case reached: {items}")
        u.auto_manual(u.auto_type)
        return items
    
    #slicing
    middle_index = len(items) // 2
    right_side = items[middle_index:]
    left_side = items[:middle_index]

    #recursion
    v.recursive_visual(indent + 1, "call", f"Left split: {items[:middle_index]}")
    u.auto_manual(u.auto_type)
    left_sorted = merge_sort(left_side, indent + 1)


    v.recursive_visual(indent + 1, "call", f"Right split: {items[middle_index:]}")
    u.auto_manual(u.auto_type)
    right_sorted = merge_sort(right_side, indent + 1)
 

    v.recursive_visual(indent + 1, "return", f"Merging results: {items}")
    u.auto_manual(u.auto_type)
    result = merge_sort_helper(right_sorted, left_sorted)
    v.recursive_visual(indent + 1, "return", f"Merging results: {result}")
    u.auto_manual(u.auto_type)

    if indent == 0:
        v.recursive_visual(0, "return", f"Final merge: {result}")
        u.auto_manual(u.auto_type)

    return result

