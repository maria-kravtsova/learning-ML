def palindrome():
    """Largest palindrome with three digits """
    palindromes = []
    for i in range(100,999):
        for j in range(100, 999):
            result = i*j
            revers = str(result)[::-1]
            if result == int(revers):
                palindromes.append(result)
            j = j + 1
    i = i + 1
    return max(palindromes)

print(palindrome())
