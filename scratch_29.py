import re

def has_vowel(string):
    return bool(re.search(r'[aeiou]', string))

print('has vowel')
print(has_vowel("rhythm"))
print(has_vowel("exit"))

print('\nis integer')
def is_integer(num):
    return bool(re.search(r'^-?[0-9]+$', num))

print(is_integer(""))
print(is_integer(" 5"))
print(is_integer("5000"))
print(is_integer("-999"))
print(is_integer("+999"))
print(is_integer("00"))
print(is_integer("0.0"))

print('\nis fraction')
def is_fraction(num):
    """
    Create a function is_fraction that accepts a string and returns True if the string represents a fraction.
    By our definition a fraction consists of:
    An optional - character
    Followed by 1 or more digits
    Followed by a /
    Followed by 1 or more digits, at least one of which is non-zero (the denominator cannot be the number 0).
    :param num:
    :return:
    """
    pattern = r'^-?\d+/\d*[1-9]+\d*$'
    return bool(re.search(pattern, num))

print(is_fraction(""))
print(is_fraction("5000"))
print(is_fraction("-999/1"))
print(is_fraction("+999/1"))
print(is_fraction("00/1"))
print(is_fraction("/5"))
print(is_fraction("5/0"))
print(is_fraction("5/010"))
print(is_fraction("5/105"))
print(is_fraction("5 / 1"))

print('\nis valid time')
def is_valid_time(time):
    """
    Create a function that returns True if given a valid 24 hour time in the format HH:MM.
    :param time:
    :return:
    """
    pattern = r'^(([01][0-9])|(2[0-3])):([0-5]\d)$'
    print(re.findall(pattern, time))
    return bool(re.search(pattern, time))

print(is_valid_time("00:19"))
print(is_valid_time("01:37"))
print(is_valid_time("10:60"))
print(is_valid_time("23:59"))
print(is_valid_time("24:00"))

print('\ndictionary:')
with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()

words = dictionary.split()
print('Find all lowercase words (no proper nouns) that include four consecutive vowels.')
for word in words:
    if re.search(r'[aeiou]{4}', word):
        print(re.search(r'[aeiou]{4}', word), end=',')
        print(word)

print(re.findall(r'\b.*[aeiou]{4}.*\b', dictionary))

print('\nFind every word that consists solely of the letters A, B, C, D, E, and F.')
for word in words:
    if re.search(r'^[ABCDEF]{1,}$', word, re.IGNORECASE):
        print(word)

print('\nFind at least one word with 6 consecutive consonants. For this problem treat y as a vowel.')
for word in words:
    if re.search(r'[^aeiou]{6,}', word):
        print(re.search(r'[^aeiou]{6,}', word), end=':')
        print(word)

print('\nMake a function possible_words that accepts a partial word with underscores representing missing letters and returns a list of all possible matches:')
def possible_words(missing_word):
    pattern = '^'+missing_word.replace('_', '.')+'$'
    for word in words:
        if re.search(pattern, word, re.IGNORECASE):
            print(word, end=',')
    print()

possible_words('CIS____')
possible_words('___TE')
possible_words('__A_S_E__')
