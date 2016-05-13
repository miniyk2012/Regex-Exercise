import re

sentence = "I'm flying the SKY wahaha"
m = re.search(r'\b[A-Z]{3}\b', sentence)

# help(m)
print(m.group())  # group返回匹配的字符串
print(m.start())
print(m.end())

# 分组()的应用
print(re.search(r'^\d{5}(-\d{4})?$', '76890-7865'))
print(re.search(r'^\d{5}(-\d{4})?$', '76890'))

m = re.search(r'(\d{5})(-\d{4})?', 'a76890-7865b')
print(m)
print(m.group())
print(m.group(1))
print(m.group(2))

# search智能找到一个匹配项,若有多个皮培训项,只找第一个匹配项
sentence = "I'm flying the SKY to KKK f III"
m = re.search(r'\b[A-Z]{3}\b', sentence)
print(m.group())

matches = re.finditer(r'\b[A-Z]{3}\b', sentence)
print(matches)
for m in matches:
    print(m)

matches = [m.group() for m in re.finditer(r'\b[A-Z]{3}\b', sentence)]
print(matches)
print('find all:')
print(re.findall(r'((\b[A-Z]{3}\b)|(\d))', "I'm flying the SKY to KKK 4f III"))

matches = [m.groups() for m in re.finditer(r'((\b[A-Z]{3}\b)|(\d))', "I'm flying the SKY to KKK 4f III")]
print(matches)

print(re.findall(r'((\d{5})(-\d{4})?)', '98766-9876\n76543'))  #  findall返回的所有不重叠的匹配,每个匹配都由若干组构成tuple.若没有组"()",就把整个pattern当成一组
print(re.findall(r'(?:\d{5})(?:-\d{4})?', '98766-9876\n76543'))  #  (?:不分组),因此返回不重叠的整个匹配字符串






