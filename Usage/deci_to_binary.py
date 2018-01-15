#By using Stack Data Struture...Convert Decimal to Binary Format....
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


decimal = 56;

stak = Stack()

while decimal > 0:
    remainder = decimal % 2
    decimal = decimal // 2
    stak.push(remainder)

bin_str = ''
while stak.size() > 0:
    bin_str += str(stak.pop())

print(bin_str)