# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.
currentNumber = 1
nextNumber = 1
numbers = []
while currentNumber < 4000000:
    currentNumber, nextNumber = nextNumber, currentNumber + nextNumber
    if currentNumber % 2 == 0:
        numbers.append(currentNumber)
print(numbers)
print(sum(numbers))
