## 1 ##

""" Using the stack reverse the order of the characters in the string 
'yesterday'"""

class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
for c in "yesterday":
    stack.push(c)

reversed_string = ""

for i in range(len(stack.items)):
    reversed_string += stack.pop()
print(reversed_string)
a_list = [1, 2, 3, 4, 5]
reversed_list = []
for i in a_list:
    stack.push(i)


## 2 ##

""" Use the stack to create a list with the contents [1, 2, 3, 4, 5], stored
in reverse order"""

for i in range(len(stack.items)):
    reversed_list.append(stack.pop())
print(reversed_list)



