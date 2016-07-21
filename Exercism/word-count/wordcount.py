import re, collections

def word_count(sentence):
    """Count the words in a sentence"""
    words = re.sub(r'[^а-яА-ЯA-Za-z0-9]', " ", sentence.lower())
    words = words.split()
    result = {}
    result = collections.Counter(words)
    return result
