# Solution can also be used for 9_1; this solution is more efficient

numPlayers = 418
lastMarble = 7076900

class Marble:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

playerScores = [0] * numPlayers # naming them from 1 to numPlayers - 1, player playerNum is saved as 0

marble0 = Marble(0)
marble1 = Marble(1)
marble0.next = marble1
marble0.prev = marble1
marble1.next = marble0
marble1.prev = marble0

current = marble1

for i in range(2, lastMarble + 1):
    if i % 23 != 0:
        marble = Marble(i)
        marble.prev = current.next
        marble.next = current.next.next
        current.next.next.prev = marble
        current.next.next = marble
        current = marble
    else:
        for j in range(7):
            current = current.prev
        playerScores[(i % numPlayers)] += (i + current.value)
        current.prev.next = current.next
        current.next.prev = current.prev
        current = current.next

# print(playerScores) -> to print end scores
print("The winning elf got a score of: " + str(max(playerScores)))
