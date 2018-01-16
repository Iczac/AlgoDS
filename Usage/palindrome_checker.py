# Palindrome Checker implementation using Deque Data Structure

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

def pdr_checker(word):

    dq = Deque()

    for char in list(word.lower()):
        dq.add_rear(char)

    occurance = 0

    initial_size = dq.size()
    if dq.size() % 2 == 0:
        while dq.size() > 0:
            if dq.remove_front() == dq.remove_rear():
                occurance += 1
        if occurance == initial_size / 2:
            return True
        else:
            return False
    else:
        while dq.size() > 1:
            if dq.remove_front() == dq.remove_rear():
                occurance += 1
        if occurance == (initial_size - 1) / 2:
            return True
        else:
            return False


print(pdr_checker('RAdAr'))
print(pdr_checker('Koterine'))


