import re, collections

def word_count(sentence):
    """Count the words in a sentence"""

    words = re.split('[\s^a-zA-Z0-9-]', sentence)
    result = collections.Counter(words)
    return result
