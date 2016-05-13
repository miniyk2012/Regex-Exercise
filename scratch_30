import re
# print(re.search(r'\b.*[aeiou]{4}.*\b', 'obsequiousnesses%').group())

with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()

print(re.findall(r'\b.*[aeiou]{4}.*\b', dictionary))  # /b:Boundary between word and non­word characters
print(re.findall(r'.*[aeiou]{4}.*', dictionary))  # .不匹配newline

print(re.findall(r'\bcis.{4}\b', dictionary))
print(re.findall(r'\b[a-f]+\b', dictionary))

print(re.search('a{2,5}', 'aaaaaa'))    # 贪婪
print(re.search('a{2,5}?', 'aaaaaa'))   # 非贪婪

print(re.findall('a{2,5}', 'aaaaaaaaaaaaa'))    # 贪婪
print(re.findall('a{2,5}?', 'aaaaaaaaaaaaa'))   # 非贪婪

print(re.search(r'\bunder\w*', 'I am underwater'))

# 匹配24小时制时间
print('匹配时间')
# print(re.search(r'\d{2}:\d{2}', '29:60'))

def is_valid_time(time):
    return re.search(r'[01]\d:[0-5]\d|2[0-3]:[0-5]\d', time)

print(is_valid_time("00:19"))
print(is_valid_time("01:37"))
print(is_valid_time("10:60"))
print(is_valid_time("23:59"))
print(is_valid_time("24:00"))

print(re.search(r'([01]\d:|2[0-3]):[0-5]\d', '23:30'))

# matching,这个比较难,可以仔细理解,主要是对findall的理解
row = '  column 1,column 2 , column 3'
print(re.findall(r'([^,]*),\s*', row))
print(re.findall(r'([^\s]+[^,]*[^\s]+)(?:\s*,\s*|\s*$)', row))

# split
print(re.split(r'\s*,\s*', 'column 1,column 2 , column 3'))

# compile
TIME_RE = re.compile(r'^([01]\d:|2[0-3]):[0-5]\d$')
print(type(TIME_RE), '\n', TIME_RE)
print(TIME_RE.search('23:89'))
print(TIME_RE.search('23:19'))

COMMA_RE = re.compile(r'([^\s]+[^,]*[^\s]+)(?:\s*,\s*|\s*$)')
print(COMMA_RE.findall(row))

# greediness
print('\ngreediness')
m = re.search(r'(".*?")', 'I say: "how are you?","dfsa"')
print(m)
print(m.groups())

sentence = """You said "How are you?". I said "I'm fine."."""
print(re.findall(r'"([^"]*)"', sentence))

print(re.findall(r'"(.*?)"', sentence)) # 非贪婪的强大应用

print()
print(re.search(r'hi?', 'hiiii'))
print(re.search(r'hi??', 'hiiii'))  # 非贪婪
print(re.search(r'hi*?a', 'hiiiia'))  # 非贪婪

