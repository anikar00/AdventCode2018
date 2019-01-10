with open("input8.txt") as file:
    data = file.readlines()[0].split(" ")
    data = list(map(int, data))

metaTotal = 0

def computeNode(data, startIndex):
    global metaTotal

    numChild = data[startIndex]
    numMeta = data[startIndex + 1]

    index = startIndex + 2
    for i in range(numChild):
        length = computeNode(data, index)
        index += length
    metaTotal += sum(data[index:(index + numMeta)])

    return index + numMeta - startIndex

computeNode(data, 0)

print(metaTotal)
