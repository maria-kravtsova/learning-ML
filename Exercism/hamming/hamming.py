def distance(stringA, stringB):
    """Calculate the different dna strands between two dna"""
    s = 0
    listA = list(stringA)
    listB = list(stringB)
    length = len(listA)
    for i in range(0, length):
        if listA[i] != listB[i]:
            s = s + 1
    return s
