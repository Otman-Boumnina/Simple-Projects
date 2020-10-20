def bubbleSort(sequence):
    indexingLength = len(sequence) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexingLength):
            if sequence[i] > sequence[i+1]:
                sorted = False 
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
    return sequence

print(bubbleSort([5,54,7,8,3,7,8,4,1,2,4,3,6,7,8,9,0,56,2,1,8,485,48,12,456,47,21,355]))