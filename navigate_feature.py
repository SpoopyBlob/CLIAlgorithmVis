import utilities as u

class Node:
    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def get_next_node(self):
        return self.next_node
    
    def get_prev_node(self):
        return self.prev_node
    
    def get_value(self):
        return self.value
    
    def set_next_node(self, node):
        self.next_node = node

    def set_prev_node(self, node):
        self.prev_node = node
    
class Navigate_Algorithm():

    def __init__(self, head_node = None, tail_node = None, list_size = 0):
        self.head_node = head_node
        self.tail_node = tail_node

    def set_nodes(self, node):
        
        if self.head_node == None:
            self.head_node = node
            self.tail_node = node
        
        elif self.head_node == self.tail_node:
            self.head_node.set_next_node(node)
            node.set_prev_node(self.head_node)
            self.tail_node = node

        else:
            self.tail_node.set_next_node(node)
            node.set_prev_node(self.tail_node)
            self.tail_node = node

    
    def add_node(self, value):
        node = Node(value)
        self.set_nodes(node)

    def clear_list(self):
        self.head_node = None
        self.tail_node = None

    #testing purposes
    def print_everything(self):
        node = self.head_node
        while node is not None:
            print(node.get_value())
            node = node.get_next_node()

Algorithm = Navigate_Algorithm()

class Transfer_Visuals:
    def __init__(self, txt = None):
        self.txt = txt

    def update_txt(self, new_txt):
        if self.txt == None:
            self.txt = new_txt
        else:
            self.txt = self.txt + new_txt

    def delete_txt(self):
        self.txt = None
    
    def push_to_node(self):
        Algorithm.add_node(self.txt)
        self.delete_txt()

    #For recursive algorithm
    def rec_push_to_node(self):
        Algorithm.add_node(self.txt)

Transfer = Transfer_Visuals()




    



        

        
    
    


    
