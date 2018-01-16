class Queue():

    def __init__(self):
        self.items = []

    def enque(self,item):
        self.items.append(item)

    def deque(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def cleanslate(self):
        self.items = []

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def contain(self,item):
        i = 0
        while i < len(self.items):
            if item == self.items[i]:
                return True
            else:
                i += 1

        return False

q = Queue()
q.enque(3)
print(q.contain(3))
print(q.deque())
print(q.contain(3))