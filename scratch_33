# Exercise老师解答

import re

def is_number(number):
    return bool(re.search(r'''
                ^
                [-+]?
                (
                    \d*\.?\d+
                    |
                    \d+\.
                )
                $
                ''', number, re.VERBOSE))


print(is_number("5"))
print(is_number("5."))
print(is_number(".5."))
print(is_number(".5"))
print(is_number("01.5"))
print(is_number("-123.859"))
print(is_number("-123.859."))
print(is_number("."))

# sub
sentence = "This is a ``smart'' quote."
print(re.sub(r"``|''", '"', sentence))

row = '   column 1,column 2, column 3'
row = re.sub(r',\s*', ',', row)
print(row)
print(re.sub(r'^\s*', '', row))

# 组引用
sentence = 'from 11/12/1908 to 05/23/1999'
print(re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2', sentence))

print(re.findall(r'["\'](.*?)["\']', "she said 'I love you'"))

sentence = '''I said "I like it". You said "I don't know"'''
print(re.findall(r'["\'](.*?)["\']', sentence))
print(re.findall(r'(["\'])(.*?)\1', sentence))

matches = re.findall(r'(["\'])(.*?)\1', sentence)
print([q for _, q in matches])

matches = re.finditer(r'(["\'])(.*?)\1', sentence)
print([m.group(2) for m in matches])


# sub 与函数
sentence = 'xx(03/09/91) yy(05/23/16)'

def replace_data(match):
    # print(match.groups())
    month ,day, year = match.groups()
    if len(year) == 4:
        year = year
    elif '00' <= year <= '50':
        year = '20' + year
    elif '50' < year <= '99':
        year = '19' + year
    return '-'.join((year, month, day))


DATE_RE = re.compile(
    r'''
    \b
    (\d{2})
    /
    (\d{2})
    /
    (\d{2}|\d{4})
    \b
    ''', re.VERBOSE)

print(DATE_RE.sub(replace_data, sentence))