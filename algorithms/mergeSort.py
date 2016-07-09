def mergeSort(array):
    """Implement merge sort"""
    if len(array) < 1:
        return array
    mid = int(len(array) / 2)
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    # mergeSort(left)
    # mergeSort(right)

    i = 0
    j = 0

    sortedArray = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedArray.append(left[i])
            i = i + 1
        else:
            sortedArray.append(right[j])
            j = j + 1
    sortedArray = sortedArray + left[i:]
    sortedArray = sortedArray + right[:i]
    print(sortedArray)

myArray = [1, 3, 8, 2, 5, 0]
mergeSort(myArray)
