#Read more about Hot Potato Game - https://runestone.academy/runestone/static/pythonds/BasicDS/SimulationHotPotato.html
#This implementation is from Rune Stone Project

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


def hot_potato(players, times):
    players = players
    times = times

    que = Queue()
    for player in players:
        que.enque(player)

    while que.size() > 1:

        for turn in range(times):
            que.enque(que.deque())
            # put back into queue as the counting hasn't end yet
        que.deque()
        # take out the times-th person out of the game
        #do this until last person

    return que.deque()

print(hot_potato(['Dave','John','Simon','David','Leon','Lilly','Tammy','Jess'],9))