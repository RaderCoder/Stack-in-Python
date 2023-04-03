import Stack

if __name__ == "__main__":
    tempstack = Stack.Stack()
    
    # print(tempstack.is_empty())

    tempstack.push(3)
    tempstack.push(4)
    tempstack.push(8)

    print("\n Size: {}".format(tempstack.size()))
    print(tempstack.head.value)

    print(tempstack)
    
    # print(tempstack.is_empty())
    
    tempstack.pop()

    print(tempstack)