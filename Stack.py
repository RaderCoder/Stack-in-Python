import LinkedList

class Stack(LinkedList.LinkedList):
    def __init__(self, head=None):
        super().__init__(head)

    def pop(self):
        self.delete_node(self.head.value)

    def top(self):
        return self.head
    
    def is_empty(self):
        return False if self.head.value else True
    
    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next

        return count

    def __repr__(self):
        temp = self.head
        repstr = "Type: Stack\n\n"

        while temp:
            repstr = repstr + str(temp.value) + "\n" + "__" + "\n"
            temp = temp.next

        return repstr