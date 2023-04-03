import Stack

if __name__ == "__main__":
    tempstack = Stack.Stack(5)

    tempstack.push(3)
    tempstack.push(4)
    tempstack.push(8)
    print(tempstack)

    tempstack.pop()

    print(tempstack)