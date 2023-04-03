### Stack Implementation in Python

This is going to be a simple stack implementation in Python. I am going to use Linked Lists instead of arrays as lists in python are already a dynamic data structure. Also Linked Lists extend to stacks pretty well depending on how the methods of the list are constructed. Notice that the pop method calls the delete_node method and we don't even need to create a push method.

#### What is a stack?

Imagine a stack of books. That's it, that's a stack. A stack is a collection of items that follow the last in first out (LIFO) principle. In essence, the value that is last inserted sits at the top of a stack. When we remove a value, the first object removed was the last object inserted.

#### Implementation

You can implement a stack using linked lists. There were two ways we could have done this. We could import the class and use it inside the stack by calling the class. However, this would be quite messy and I decided to inherit the Linked List instead. It simplifies our task as sharing the methods will ease some of the functions of the stack. Notice that the head value is essentially the top value and the push function doesn't even need modification. Also notice that we call the delete function in the pop method.

#### Functions of Stacks

- push: Inserts a value into the stack. The push method we inherited from the linked list is perfect for this operation. In a stack, we insert a value at the top. The inherited push method inserts values at the head of the list, which will be the top of the stack.
- pop: Pops the top value of the stack. As we are inheriting from a linked list, we have a lot of crossover for the methods. We call the delete node method with the head value as parameters.
- size: Returns the size of the stack. Simply iterate over the list.
- top: Returns the top value of the stack. Simply return the head of the stack.
- is_empty: Returns true if the stack is empty, otherwise false. Checking the head value will suffice. If there is no head for the stack, there are no other nodes, hence the stack is empty.