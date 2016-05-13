import re
greeting = 'hello world'

print(re.search(r'[a-z]', greeting))
print(re.search(r'[^0-9]', '$100'))
print(re.search(r'^\$', '$a100'))
print(re.search(r'\[hello\]', 'b[hello]a'))  # \[用来匹配'['
print(re.search(r'\d+', '$100'))
print(re.search(r'\D+', '100$s'))
print(re.search(r'\D+?', '100$s'))  # 非贪婪
print(re.search(r'', '100$s'))
print('new_line' + '\n')
print('tab' + '\t')
print(re.search(r'\s*', "\n\t\t "))
print(re.search(r'\S+', " \t \ndfa"))
print(re.search(r'\bhello\b', 'afds hello'))
print(re.search(r'\bhello\b', 'afds hello_'))
print(re.search(r'^\d{5}$', '45677'))
print(re.search(r'^\d{3,5}$', '456'))
print(re.search(r'^\d{,3}$', '45'))
print(re.search(r'^\d{3,}$', '4568389989889'))
print(re.search(r'^\d{,}$', '4568389989889'))
print(re.search(r'^\d*$', ''))
print(re.search(r'^\d{,}$', ''))

# Flag
print(re.search('hello', 'Hello world', re.IGNORECASE))
print(re.search('[A-Z]', 'hello world', re.IGNORECASE))

def is_valid_uudi(uuid):
    hex_re = r'[ a-f \d ]'
    return bool(re.search(r'''
    ^
    {hex} {{8}}
    $
    '''.format(hex=hex_re), uuid, re.IGNORECASE | re.VERBOSE))

print(is_valid_uudi('aeb12345'))
print(is_valid_uudi('aeb12x45'))
