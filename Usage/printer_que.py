# Simple Printer queue system Implementation using Python with Queue Data Structure

import time

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

    def isEmpty(self):
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

class Printer():
    def __init__(self):
        self.print_ques = Queue()

    def jobs(self):
        return self.print_ques.size()

    def accept_print(self,pages):
        self.print_ques.enque(pages)

    def calculate_current_task(self):
        self.task_time = self.print_ques.peek() * 3
        return self.task_time

    def print(self):
        print('Preparing to Print')
        for item in list(range(1,self.print_ques.peek())):
            time.sleep(3)
            print('Printing Page Number ' + str(item))
            time.sleep(2)
        self.print_ques.deque()
        print('Printing Completed')

printer = Printer()
printer.accept_print(5)

while printer.jobs() > 0:
    print('Current Printing Task will take approximately ' + str(printer.calculate_current_task()) + 'seconds')
    printer.print()
