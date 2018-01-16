# Some Linked List coding Challenges

class Node():

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

    def set_previous(self, value):
        self.previous = value

    def get_previous(self):
        return self.previous

    def set_next(self, value):
        self.next = value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def remove_value(self):
        self.value = None

print()
# 1 - Traverse a linked list
node1 = Node(3)
node2 = Node(6)
node3 = Node(1)
node4 = Node(2)
node5 = Node(8)
node6 = Node(9)
node7 = Node(3)
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
node4.set_next(node5)
node5.set_next(node6)
node6.set_next(node7)
print('------------------------------')
print('----Traverse A Linked List----')
print('------------------------------')
print(' ')

node = node1

while node != None:
    print(node.get_value())
    node = node.next

print(' ')
print('________________The End_________________')
print(' ')
print(' ')
print(' ')
# 2 - Remove duplicates from a linked list
node1 = Node(3)
node2 = Node(6)
node3 = Node(1)
node4 = Node(2)
node5 = Node(8)
node6 = Node(9)
node7 = Node(3)
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
node4.set_next(node5)
node5.set_next(node6)
node6.set_next(node7)
print('--------------------------------------------')
print('----Remove Duplicates from a Linked List----')
print('--------------------------------------------')
print(' ')

node = node1
initial_array = []

while node != None:
    initial_array.append(node.get_value())
    node = node.get_next()

print('Original Array - ' + str(initial_array))

node = node1
node_arr = []
dup_arr = []

while node != None:
    node_value = node.get_value()
    if node_value in node_arr:
        dup_arr.append(node_value)
        node.remove_value()
    else:
        node_arr.append(node_value)
    node = node.next

print('Removed Duplicates - ' + str(dup_arr))
print('Duplicates Free Array - ' + str(node_arr))

print(' ')
print('________________The End_________________')
print(' ')
print(' ')
print(' ')


# 3 - Get the kth to last element from a linked list
node1 = Node(3)
node2 = Node(6)
node3 = Node(1)
node4 = Node(2)
node5 = Node(8)
node6 = Node(9)
node7 = Node(3)
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
node4.set_next(node5)
node5.set_next(node6)
node6.set_next(node7)
print('------------------------------------------------------')
print('----Get the kth to Last Element from a Linked List----')
print('------------------------------------------------------')
print(' ')

k = 3

node = node1
initial_array = []

while node != None:
    initial_array.append(node.get_value())
    node = node.get_next()

print('k Value - ' + str(k))

print('Original Array - ' + str(initial_array))


node = node1
node_arr = []
dup_arr = []

while node != None:
    node_value = node.get_value()
    node_arr.append(node_value)
    node = node.next

print('Spliced Array - ' + str(node_arr[k:]))

print(' ')
print('________________The End_________________')
print(' ')
print(' ')
print(' ')

# 4 - Delete a Node from a Linked List
node1 = Node(3)
node2 = Node(6)
node3 = Node(1)
node4 = Node(2)
node5 = Node(8)
node6 = Node(9)
node7 = Node(3)
node1.set_next(node2)
node2.set_previous(node1)
node2.set_next(node3)
node2.set_previous(node2)
node3.set_next(node4)
node2.set_previous(node3)
node4.set_next(node5)
node2.set_previous(node4)
node5.set_next(node6)
node2.set_previous(node5)
node6.set_next(node7)
node2.set_previous(node6)
print('----------------------------------------')
print('----Delete a Node from a Linked List----')
print('----------------------------------------')
print(' ')


key = 3
node = node1
initial_array = []

while node != None:
    initial_array.append(node.get_value())
    node = node.get_next()

node = node1
deleted_array = []

while node != None:
    node_value = node.get_value()
    if node_value == key:
        prev = node.get_previous()
        next = node.get_next()

        if prev != None:
            prev.set_next(next)

        if next != None:
            next.set_previous(prev)

        node.remove_value()
        node = node.get_next()
    else:
        deleted_array.append(node_value)
        node = node.get_next()

print('Before Deletion - ' + str(initial_array))
print('After Deletion - ' + str(deleted_array))


print(' ')
print('________________The End_________________')
print(' ')
print(' ')


# 5 - Adding Linked List Values from Left to Right
node1 = Node(3)
node2 = Node(6)
node3 = Node(1)
node4 = Node(2)
node5 = Node(8)
node6 = Node(9)
node7 = Node(3)
node1.set_next(node2)
node2.set_previous(node1)
node2.set_next(node3)
node2.set_previous(node2)
node3.set_next(node4)
node2.set_previous(node3)
node4.set_next(node5)
node2.set_previous(node4)
node5.set_next(node6)
node2.set_previous(node5)
node6.set_next(node7)
node2.set_previous(node6)
print('----------------------------------------')
print('----Delete a Node from a Linked List----')
print('----------------------------------------')
print(' ')

node = node1
sum_array = []

while node != None:
    sum_array.append(node.get_value())
    node = node.get_next()

result = 0
for item in sum_array:
    print('Adding ' + str(item) + ' to Result')
    result += item

print('Total is ' + str(result))

print(' ')
print('________________The End_________________')
print(' ')
print(' ')


# 6 - Adding Linked List Values from Right to Left
node1 = Node(3)
node2 = Node(6)
node3 = Node(1)
node4 = Node(2)
node5 = Node(8)
node6 = Node(9)
node7 = Node(3)
node1.set_next(node2)
node2.set_previous(node1)
node2.set_next(node3)
node2.set_previous(node2)
node3.set_next(node4)
node2.set_previous(node3)
node4.set_next(node5)
node2.set_previous(node4)
node5.set_next(node6)
node2.set_previous(node5)
node6.set_next(node7)
node2.set_previous(node6)
print('----------------------------------------')
print('----Delete a Node from a Linked List----')
print('----------------------------------------')
print(' ')

node = node1
sum_array = []

while node != None:
    sum_array.append(node.get_value())
    node = node.get_next()

result = 0
for item in sum_array[::-1]:
    print('Adding ' + str(item) + ' to Result')
    result += item

print('Total is ' + str(result))

print(' ')
print('________________The End_________________')
print(' ')
print(' ')