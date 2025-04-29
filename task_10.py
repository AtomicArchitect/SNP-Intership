import re

def count_words(string):
    if string is None: return None
    if len(string) == 0 or len(string) == 1: return None
    string = re.sub(r'[^a-zA-Z0-9\s]', '', string)
    words = string.lower().split()
    words_count = dict()
    for word in words:
        if word in words_count: words_count[word] += 1
        else: words_count[word] = 1
    return words_count

assert count_words("A man, a plan, a canal -- Panama") == {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}
assert count_words("Doo bee doo bee doo") == {"doo": 3, "bee": 2}
