import LinkedList

class Stack(LinkedList.LinkedList):
    def __init__(self, head=None):
        super().__init__(head)

    def pop(self):
        self.delete_node(self.head.value)
