# Deque Data Structure also known as Deck

class Deque():

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop(0)

    def add_rear(self, item):
        self.items.append(item)

    def remove_rear(self):
        return self.items.pop(len(self.items)-1)

    def size(self):
        return len(self.items)

    def peek_front(self):
        return self.items[0]

    def peek_rear(self):
        return self.items[len(self.items)-1]

    def cleanslate(self):
        self.items = []

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def contain(self, item):
        i = 0
        while i < len(self.items):
            if item == self.items[i]:
                return True
            else:
                i += 1

        return False


dq = Deque()
dq.add_front(1)
dq.add_rear(3)
dq.add_front('Hello')
dq.add_front(9)
print(dq.size())
print(dq.contain(9))
print(dq.is_empty())
print(dq.peek_front())
print(dq.peek_rear())
dq.remove_front()
dq.remove_rear()
print(dq.peek_front())
print(dq.peek_rear())