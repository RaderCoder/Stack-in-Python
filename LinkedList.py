class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = Node(head)

    def push(self, new_data):
        if self.head.value:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
        else:
            self.head.value = new_data

    def find_value(self,value):
        temp = self.head
        found = False
        while temp:
            if temp.value == value:
                found = True
                break
            else:
                temp = temp.next
        
        return found
    
    def delete_node(self, value):
        if self.find_value(value):
            temp = self.head
            prev = None
            found = False
            while temp:
                if temp.value == value:
                    found = True
                    break
                else:
                    prev = temp
                    temp = temp.next
            
            if prev: # If there is a previous value, then we are not deleting the head, thus no need to change it
                prev.next = temp.next
                temp.next = None
            else:
                self.head = temp.next
                temp.next = None

        else:
            return "Value not found"


    def __repr__(self):
        repstr = ""
        temp = self.head
        
        while temp:
            repstr = repstr + str(temp.value) + " -> "
            temp = temp.next

        return repstr