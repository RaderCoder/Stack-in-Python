import LinkedList

class Stack(LinkedList.LinkedList):
    def __init__(self, head=None):
        super().__init__(head)

    def pop(self):
        self.delete_node(self.head.value)

    def __repr__(self):
        temp = self.head
        repstr = "Type: Stack\n\n"

        while temp:
            repstr = repstr + str(temp.value) + "\n" + "__" + "\n"
            temp = temp.next

        return repstr