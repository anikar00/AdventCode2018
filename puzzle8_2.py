with open("input8.txt") as file:
    data = file.readlines()[0].split(" ")
    data = list(map(int, data))

def computeValue(data, startIndex):
    numChild = data[startIndex]
    numMeta = data[startIndex + 1]

    index = startIndex + 2
    vals = {}
    for i in range(numChild):
        [length, val] = computeValue(data, index)
        index += length
        vals[i + 1] = val

    value = 0
    if numChild == 0:
        value = sum(data[index:(index + numMeta)])
    else:
        metaData = data[index:(index + numMeta)]
        for m in metaData:
            value += vals.get(m, 0)

    return [index + numMeta - startIndex, value]


rootValue = computeValue(data, 0)[1]

print(rootValue)
