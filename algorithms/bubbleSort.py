def bubble_sort(array):
    """Bubble Sort a list"""
    sortedArray = False
    length = len(array) - 1
    while not sortedArray:
        sortedArray = True
        for i in range(0, length):
            if array[i] > array[i+1]:
                # Swap elements
                array[i], array[i+1] = array[i+1], array[i]
                sortedArray = False
    print(array)
bubble_sort([1, 2, 0, 5, 4, 6])
