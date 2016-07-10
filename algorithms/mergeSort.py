def divide(array):
    """Divide the array"""
    length = int(len(array))
    if length == 0 or length == 1:
        return array
    else:
        mid = int(length / 2)
        left = array[:mid]
        right = array[mid:]
        left = divide(left)
        right = divide(right)
        print(left, right)
        return conquer(left, right)

def conquer(left, right):
    """Sort and merge"""
    sortedArray = []
    i, j = 0, 0
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            sortedArray.append(left[i])
            i += 1
        else:
            sortedArray.append(right[j])
            j += 1

    while i < len(left):
        sortedArray.append(left[i])
        i += 1
    while j < len(right):
        sortedArray.append(right[j])
        j += 1

    return(sortedArray)

myArray = [1, 3, 8, 2, 5, 0]
print(divide(myArray))
