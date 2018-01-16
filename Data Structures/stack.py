class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(len(self.items) - 1)

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)


stak = Stack()
stak.push(5)
print(stak.pop())
