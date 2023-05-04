def quicksort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    item_g = []
    item_l = []
    for item in sequence:
        if item > pivot:
            item_g.append(item)
        else:
            item_l.append(item)

    return quicksort(item_l) + [pivot] + quicksort(item_g)

print(quicksort([1,5,3,6,2,5,33,66,3,9]))