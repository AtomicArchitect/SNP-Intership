import re

def is_palindrome(source):
    if source is None: return False
    elif type(source) == int: source = str(source)
    if len(source) == 0 or len(source) == 1: return True
    source = re.sub(r'[^a-zA-Z0-9]', '', source)
    source = source.lower()
    left = 0
    right = len(source) - 1
    while left < right:
        if source[left] == source[right]:
            left += 1
            right -= 1
        else: return False
    return True

assert is_palindrome("A man, a plan, a canal -- Panama") == True
assert is_palindrome("Madam, I'm Adam!") == True
assert is_palindrome(333) == True
assert is_palindrome(None) == False
assert is_palindrome("Abracadabra") == False