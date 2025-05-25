import algorithm as a
import utilities as u
import visual as v
import navigate_feature  as n


def linear_search_setup():
    list_size = list_size_setup()
    items, target = u.random_list_generator_target(list_size)
    a.linear_search(items, target)
    navigate_algorithm()
       

def naive_pattern_search_setup():
    string = input("Enter string: ")
    target = input("Enter target: ")

    a.naive_pattern_search(string, target)
    navigate_algorithm()

def bubble_sort_setup():
    list_size = list_size_setup()
    
    if list_size == False:
        return

    a.bubble_sort(u.random_list_generator(list_size))
    navigate_algorithm()

def merge_sort_setup():
    list_size = list_size_setup()
    a.merge_sort(u.random_list_generator(list_size))
    navigate_algorithm()
    n.Transfer.delete_txt()


def auto_manual_mode():
    while True:
        u.system_clear()
        v.auto_manual_print()

        user_input = input("Enter here: ")

        if user_input == "0":
            u.auto_type = 0 #auto
            v.format_string("auto_manual = ", "auto")
            u.auto_manual()
            break

        elif user_input == "1":
            u.auto_type = 1 #manual
            v.format_string("auto_manual = ", "manual")
            u.auto_manual()
            break

        elif user_input == "2":
            return
        
        else:
            v.error_message("Invalid Input!")
            u.auto_manual()

def auto_speed():
    while True:
        speed = input("Enter auto speed between 1 to 5: ")
        
        try:
            auto_speed = int(speed)
        except ValueError:
            v.error_message("Please enter a valid number!")
            u.auto_manual(mod = 1)
            continue

        if auto_speed < 1 or auto_speed > 5:
            v.error_message("Pick a number between 1 & 5")
            u.auto_manual(mod = 1)
            continue

        u.auto_speed = auto_speed
        v.format_string("auto_speed = ", u.auto_speed)
        u.auto_manual()
        break

def colour_legend_setup():
    while True:
        v.colour_legend_print()
        user_input = input("Enter here: ")

        if user_input.lower() == "e":
            v.system_message("No changes made!")
            u.auto_manual()
            return
        
        parts = user_input.split()

        if length_validation(parts, 3):
            continue

        parts = safe_str_to_int_validation(parts)
        if parts == False:
            continue
        

        if range_validation_list(parts, 0, 8):
            continue

        u.colour_change(parts)
        break

def length_validation(items, length):

    if len(items) != length:
        v.error_message(f"Your length {len(items)}, required length {length}")
        u.auto_manual(mod = 1)
        return True
    
    return False

def range_validation_list(items, start_range, end_range):

    if not all(start_range <= i < end_range for i in items):
        v.error_message(f"Please select the items between {start_range} and {end_range - 1}")
        u.auto_manual(mod = 1)
        return True
    
    return False

def range_validation(item, start_range, end_range):

    if not start_range <= item < end_range:
        v.error_message(f"Please select the items between {start_range} and {end_range - 1}")
        u.auto_manual(mod = 1)
        return True
    
    return False


def safe_str_to_int_validation(items):
    
    if isinstance(items, list):
        try:
            items = [int(i) for i in items]
    
        except ValueError:
            v.error_message("Please use intergers, not any other character")
            u.auto_manual(mod = 1)
            return False
    
    else:
        try:
            items = int(items)
        
        except ValueError:
            v.error_message("Please use intergers, not any other character")
            u.auto_manual(mod = 1)
            return False


    return items


def list_size_setup():
    while True:
        list_size = input("Enter list size between 1 - 10 or e to exit: ")

        if list_size == "e":
            return False

        list_size = safe_str_to_int_validation(list_size)
        
        if list_size == False:
            continue

        if range_validation(list_size, 1, 11):
            continue

        return list_size
    
def navigate_algorithm():
    node = n.Algorithm.tail_node

    while True:
        u.system_clear()
        print(node.get_value())
        v.navigate_print()
        user_input = input("")
        
        if user_input == "0":
            if node.get_prev_node() == None:
                v.error_message("Can't go further")
                u.auto_manual()
                continue
            else:
                node = node.get_prev_node()
                continue

        if user_input == "1":
            if node.get_next_node() == None:
                v.error_message("Can't go further")
                u.auto_manual()
                continue
            else:
                node = node.get_next_node()
                continue

        if user_input.lower() == "e":
            n.Algorithm.clear_list()
            break


    

