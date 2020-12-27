def quickSort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    itemsGreater = []
    itemsLower = []

    for item in sequence:
        if item > pivot:
            itemsGreater.append(item)
        else:
            itemsLower.append(item)
    return quickSort(itemsLower) + [pivot] + quickSort(itemsGreater)

print(quickSort([5,54,7,8,3,7,8,4,1,2,4,3,6,7,8,9,0,56,2,1,8,485,48,12,456,47,21,355]))
