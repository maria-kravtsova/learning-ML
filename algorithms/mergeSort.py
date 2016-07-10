def divide(array):
    """Divide the array"""
    length = int(len(array))
    if length > 1:
        mid = int(length / 2)
        left = array[:mid]
        right = array[mid:]
        divide(left)
        divide(right)
        # print(left, right)
        return conquer(left, right)
    else:
        return array

def conquer(left, right):
    """Sort and merge"""
    sortedArray = []
    i, j = 0, 0
    while (len(left) > i) and (len(right) > j):
        if left[i] < right[j]:
            sortedArray.append(left[i])
            print(left[i], right[j])
            print("Sorted ", sortedArray)
            i = i + 1
        else:
            sortedArray.append(right[j])
            print(left[i], right[j])
            print("Sorted ", sortedArray)
            j = j + 1

    sortedArray += left[i:]
    sortedArray += right[j:]

    print(sortedArray)
    return sortedArray

myArray = [1, 3, 8, 2, 5, 0]
print(divide(myArray))
