class Node():

    def __init__(self, value=None):
        self.value = value
        self.next = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def remove_value(self, value):
        self.value = None

    def set_next(self, value):
        self.next = value

node1 = Node()
node2 = Node()
node3 = Node()
node1.set_value(3)
node1.set_next(node2)
node2.set_value(6)
node2.set_next(node3)
node3.set_value(10)

node = node1

while node != None:
    print(node.get_value())
    node = node.next