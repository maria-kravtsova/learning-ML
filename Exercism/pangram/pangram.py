def is_pangram(sentence):
    """Check if a sentence is using every letter of the alphabet at least once"""
    alphabet = 'abcdefghijklmnopqrstvxyz'
    for letter in alphabet:
        if letter not in sentence.lower():
            return False
    return True
