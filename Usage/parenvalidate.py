#By using Stack Data Struture...Validate Parentheses Usage....

class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(len(self.items) - 1)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

paren_str = '{}[]({})[[(](]))'

paren_str_list = list(paren_str)

stak = Stack()

for item in paren_str_list:
    if item in '({[':
        stak.push('P')
    elif item in ')}]':
        stak.pop()
    else:
        print('!@#$%^&*()')

if stak.size() == 0:
    print('Validation Successful.')
else:
    print('Validation Failed. Please Check Your Parentheses.')

