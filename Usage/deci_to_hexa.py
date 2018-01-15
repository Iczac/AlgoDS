#By using Stack Data Struture...Convert Decimal to Hexadecimal Value....

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

decimal = 53123

stak = Stack()

hexa_digits = '0123456789ABCDEF'

while decimal > 0:
    remainder = decimal % 16
    decimal = decimal // 16
    stak.push(remainder)

bin_str = ''
while stak.size() > 0:
    bin_str += hexa_digits[stak.pop()]

print(bin_str)