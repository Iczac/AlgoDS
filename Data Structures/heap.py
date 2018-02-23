class Node:
    def __init__(self, id, key, edge, isX, index=9999):
        self.id = id
        self.key = key
        self.edge = edge
        self.isX = isX
        self.index = index

    # reload > sign
    def __gt__(self, other):
        print self.key
        print other.key
        print ""
        if self.key > other.key:
            return True
        else:
            return False


    def __repr__(self):
        return str("\nid\t" + str(self.id) + \
                "\nkey\t" + str(self.key) + \
                "\nedge\t" + str(self.edge) + \
                "\nisInX\t" + str(self.isX) + \
                "\nindex\t" + str(self.index) + "\n\n")

class Heap:
    """
    maximum heap data structure
    1) pop the minimum item in O(logN)
    2) push an item in O(logN)
    """

    def __init__(self, initlist=[]):
        self.heaplist = initlist

    def delete(self, index):
        """delete the index item and move the last item to this index,
        and then try bubbledown. if bubbledown does nothing, try bubbleup"""

        # if delete the last, do it directly
        if len(self.heaplist) == index + 1:
            del self.heaplist[-1]
            return

        self.heaplist[index] = self.heaplist[-1]
        self.heaplist[index].index = index

        del self.heaplist[-1]
        if len(self.heaplist) <= 0:
            return

        temp = self.heaplist[index]
        self.bubbledown(index)
        if self.heaplist[index] == temp:
            self.bubbleup(index)

        return

    def getmin(self):
        retitem = self.heaplist[0]

        if len(self.heaplist) == 1:
            del self.heaplist[-1]
            return retitem

        self.heaplist[0] = self.heaplist[-1]
        self.heaplist[0].index = 0
        del self.heaplist[-1]
        self.bubbledown(0)

        return retitem

    def push(self, item):
        item.index = len(self.heaplist)
        self.heaplist.append(item)
        self.bubbleup(len(self.heaplist) - 1)

    def bubbleup(self, index):
        """recursively check if the index node is smaller than it's parent,
        if true, exchange the value"""

        if index <= 0:
            return

        parent = (index - 1) / 2
        if self.heaplist[index] < self.heaplist[parent]:
            self.heaplist[index], self.heaplist[parent] = self.heaplist[parent], self.heaplist[index]

            # set the index of the exchanged two nodes
            self.heaplist[index].index = index
            self.heaplist[parent].index = parent

            self.bubbleup(parent)

        return

    def bubbledown(self, index):
        """recursively check if the index node is smaller than it's child,
        if not exchange the value"""

        # no right child
        if len(self.heaplist) <= index * 2 + 2:
            # no right child and left child
            if len(self.heaplist) <= index * 2 + 1:
                return

            # no right but has left
            else:
                # left > index
                if self.heaplist[index] > self.heaplist[index * 2 + 1]:
                    self.heaplist[index], self.heaplist[index * 2 + 1] = \
                        self.heaplist[index * 2 + 1], self.heaplist[index]

                    # set the index of the exchanged two nodes
                    self.heaplist[index].index = index
                    self.heaplist[index * 2 + 1].index = index * 2 + 1

                    self.bubbledown(index * 2 + 1)

                # left <= index
                else:
                    return

        # has right child
        else:
            smallerone = (index * 2 + 1) if self.heaplist[index * 2 + 1] < self.heaplist[index * 2 + 2] \
                else (index * 2 + 2)

            # index > the smaller one of the two child
            if self.heaplist[index] > self.heaplist[smallerone]:
                self.heaplist[index], self.heaplist[smallerone] = self.heaplist[smallerone], self.heaplist[index]

                # set the index of the exchanged two nodes
                self.heaplist[index].index = index
                self.heaplist[smallerone].index = smallerone

                self.bubbledown(smallerone)

        return
