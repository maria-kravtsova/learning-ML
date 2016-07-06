# Calculate the sum of the multiples of 3 or 5
numbers = []
for number in range(0, 1000):
    if number % 3 == 0 or number % 5 == 0:
        numbers.append(number)
print(sum(numbers))
