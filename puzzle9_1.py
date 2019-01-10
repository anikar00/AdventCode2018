numPlayers = 418
lastMarble = 70769

board = [0]
currentIndex = 0
playerTurn = 1
playerScores = {}

for p in range(numPlayers):
    playerScores[p + 1] = 0

for i in range(1, lastMarble + 1):
    if i % 23 != 0:
        currentIndex = (currentIndex + 2) % len(board)
        if currentIndex == 0:
            currentIndex = len(board)
        board.insert(currentIndex, i)
    else:
        currentIndex = currentIndex - 7
        if currentIndex < 0:
            currentIndex = len(board) + currentIndex
        playerScores[playerTurn] += (board.pop(currentIndex) + i)
        if currentIndex == len(board):
            currentIndex = 0

    playerTurn = (playerTurn + 1) % numPlayers
    if playerTurn == 0:
        playerTurn = numPlayers

    # print(str(i) + ": " + str(board)) -> to print out board

# print(playerScores) -> to print end scores
print("The winning elf got a score of: " + str(max(playerScores.values())))
