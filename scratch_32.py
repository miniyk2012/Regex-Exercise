# Exercise2
import re

print('number')
def is_number(number):
    # Write a function to match decimal numbers.
    # We want to allow an optional - and we want to match numbers with or without one decimal point:
    NUM_RE = re.compile(r'^-*(\d+\.|\.\d+|\d+.\d+|\d+)$')
    print(NUM_RE.search(number), end=':')
    return bool(NUM_RE.search(number))

print(is_number("5"))
print(is_number("5."))
print(is_number(".5."))
print(is_number(".5"))
print(is_number("01.5"))
print(is_number("-123.859"))
print(is_number("-123.859."))
print(is_number("."))

print('\nhex color')
def is_hex_color(color):
    # Write a function to match hexadecimal color codes.
    # Hex color codes consist of an octothorpe symbol followed by either 3 or 6 hexadecimal digits (that's 0 to 9 or a to f).
    HEX_RE = re.compile(r'^#([\da-f]{6}|[\da-f]{3})$', re.IGNORECASE)
    print(HEX_RE.search(color), end=': ')
    return bool(HEX_RE.search(color))

print(is_hex_color("#639"))
print(is_hex_color("#6349"))
print(is_hex_color("#63459"))
print(is_hex_color("#634569"))
print(is_hex_color("#663399"))
print(is_hex_color("#000000"))
print(is_hex_color("#00"))
print(is_hex_color("#FFffFF"))
print(is_hex_color("#decaff"))
print(is_hex_color("#decafz"))

with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()

print('\nPalindromes回文')
PAL_RE = re.compile(r'\b((.)(.).\3\2)\b')
print([ele[0] for ele in PAL_RE.findall(dictionary)])

print('\nDoubleDouble')
DOUBLE_RE = re.compile(r'(\b.*((.)\3).\2.*\b)')
print([ele[0] for ele in DOUBLE_RE.findall(dictionary)])  # 好丑

print('\nRepetitive Words')
REP_RE = re.compile(r'\b((.{2,})\2)\b')
print([ele[0] for ele in REP_RE.findall(dictionary)])
REP_RE = re.compile(r'\b(?P<total>(?P<name>.{2,})(?P=name))\b')
print([ele.group('total') for ele in REP_RE.finditer(dictionary)])  # 分组命名,可以用一下哟

print('\nSubstitution Exercises')

print('Get File Extension')
def get_extension(filename):
    """
    Make a function that accepts a full file path and returns the file extension.
    :param filename:
    :return: extension
    """
    EXTEN_RE = re.compile(r'.*\.(.*)$')
    return EXTEN_RE.search(filename).group(1)
    pass

print(get_extension('archive.zip'))
print(get_extension('image.jpeg'))
print(get_extension('index.xhtml'))
print(get_extension('archive.tar.gz'))

print('\nNormalize JPEG Extension')
def normalize_jpeg(filename):
    """
    Make a function that accepts a JPEG filename and returns a new filename with jpg lowercased without an e.
    :param filename:
    :return:
    """
    JPG_RE = re.compile(r'(.*\.)(jp[e]?g)$', re.IGNORECASE)
    return JPG_RE.sub(r'\1jpg', filename)

print(normalize_jpeg('avatar.jpeg'))
print(normalize_jpeg('Avatar.JPEG'))
print(normalize_jpeg('AVATAR.Jpg'))
print(normalize_jpeg('AVATAR.xx.JpG'))

print('\nNormalize Whitespace')
def normalize_whitespace(sentence):
    """
    Make a function that replaces all instances of one or more whitespace characters with a single space:
    :param sentence:
    :return:
    """
    s = re.sub(r'\s+', r' ', sentence)
    return re.sub(r'\s+$', '', s)   # 去除结尾的空格

print(normalize_whitespace("hello  there"))
print(normalize_whitespace("""Hold fast to dreams
For if dreams die
Life is a broken-winged bird
That cannot fly.

 Hold fast to dreams
 For when dreams go
 Life is a barren field
 Frozen with snow.   """))

print('\nCompress blank links')
def compress_blank_lines(lines, max_blanks):
    """
    Write a function that accepts a string and an integer N and
    compresses runs of N or more consecutive empty lines into just N empty lines.
    :param lines:
    :return:
    """
    print('*'*100)
    COMPRESS_RE = re.compile(r'\n{%s,}'%(max_blanks+1))
    return COMPRESS_RE.sub(r'\n'*(max_blanks+1), lines)
    pass

print(compress_blank_lines("a\n\nb", max_blanks=1))
print(compress_blank_lines("a\n\nb", max_blanks=0))
print(compress_blank_lines("a\n\n\n\nb", max_blanks=2))
print(compress_blank_lines("a\n\n\n\n\nb\nc", max_blanks=2))

print(r'\nNormalize URL')
def normalize_domain(url):
    """
    I own the domain treyhunner.com. I prefer to link to my website as https://treyhunner.com, but I have some links that use http or use a www subdomain.
    Write a function that normalizes all www.treyhunner.com and treyhunner.com links to use HTTPS and remove the www subdomain.
    :param url:
    :return:
    """
    url1 = re.sub(r'^http[s]?', r'https', url)
    url2 = re.sub(r'(://)(www.)', r'\1', url1)
    return url2

print(normalize_domain("http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/"))
# 'https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/'
print(normalize_domain("https://treyhunner.com/2016/02/how-to-merge-dictionaries-in-python/"))
# 'https://treyhunner.com/2016/02/how-to-merge-dictionaries-in-python/'
print(normalize_domain("http://www.treyhunner.com/2015/11/counting-things-in-python/"))
# 'https://treyhunner.com/2015/11/counting-things-in-python/'
print(normalize_domain("http://www.treyhunner.com"))
# 'https://treyhunner.com'
print(normalize_domain("http://trey.in/give-a-talk"))
# 'http://trey.in/give-a-talk'

print(r'Linebreaks')
def convert_linebreaks(text):
    """
    Write a function that accepts a string and converts linebreaks to HTML in the following way:
        text is surrounded by paragraphs
        text with two line breaks between is considered two separate paragraphs
        text with a single line break between is separated by a <br>
    :param text:
    :return:
    """
    print('*'*100)
    text1 = re.sub(r'([^\n])(\n)([^\n])', r'\1<br>\3', text)
    text2 = re.sub(r'([^\s]+)', r'<p>\1<p>', text1)
    return re.sub(r'\s+', r'', text2)
    pass


print(convert_linebreaks("hello"))
# '<p>hello</p>'
print(convert_linebreaks("hello\nthere"))
# '<p>hello<br>there</p>'
print(convert_linebreaks("hello\n\nthere"))
# '<p>hello</p><p>there</p>'
print(convert_linebreaks("hello\nthere\n\nworld"))
# '<p>hello<br>there</p><p>world</p>'

# 找到所有word
sentence = "Oh what a day, what a lovely day! what kdfa what d"
print(re.findall(r'\b\w+\b', sentence))

# 找到相同的两个单词
print(re.findall(r'\b(\w+)\b.*?\b\1\b', sentence))  # 非贪婪
print(re.findall(r'\b(\w+)\b.*\b\1\b', sentence))  # 贪婪

print('\nLookahead Exercises')
# 不消耗字符串,而只往后看,用到Lookahead
sentence = "Oh what  a day, what a lovely day! ni hao ya"
print(re.findall(r'\b(\w+)\b(?=.*\b\1\b)', sentence))  # 不消耗字符串(?=), Zero-width match confirming abc will match upcoming chars

print(re.findall(r'(.)x', 'axxxx'))
print(re.findall(r'(.)(?=x)', 'axxxx')) # 找出所有后面跟着x的字母,用lookahead,这样才会不会消耗后面跟随的x

print('\nnegative lookahead')
print(re.findall(r'([a-z]).*\1', 'aba bcc'))  # 找到相同的字母
print(re.findall(r'([a-z]).*(?!\1)', 'a'))
print(re.findall(r'([a-z]).*(?!\1)', 'a '))
print(re.search(r'([a-z]).*(?!\1)[a-z]', 'ab'))  # 这个理解比较难,这里的意思是,紧跟着的字母不能和前面的[a-z]相同,这是因为(?!不消耗字母!)
print(re.search(r'([a-z]).*(?!\1)[a-z]', 'aa'))
print(re.search(r'([a-z]).*(?!\1)[a-z]', 'a b'))
print(re.search(r'([a-z]{2}).*(?!\1)[a-z]{2}', 'abac'))  # 这里的意思是,后面2个字母不能和前面的2个字母相同,这是因为(?!不消耗字母!)
print(re.search(r'([a-z]{2}).*(?!\1)[a-z]{2}', 'abab'))  # 这里的意思是,后面2个字母不能和前面的2个字母相同,这是因为(?!不消耗字母!)


def normarize_whitespace(string):
    return re.sub(r'\s*', ' ', string)  # 替换的含义是找到所有匹配项,每个匹配项替换成所要求的形式.这里消耗一个字母就找到一个0长度的\s,然后将其替换成空格
print(normarize_whitespace('hello  \n  world'))



print(re.findall(r'\b((?=.*a.*)(?=.*i.*).{3})\b', dictionary))
print(re.findall(r'\b((?=.*a.*)(?=.*e.*)(?=.*i.*)(?=.*o.*)(?=.*u.*).{1,9})\b', dictionary))  # 因为lookahead不消耗字母,因此就具有了任意顺序的功能

def all_vowels_words(dictionary):
    """
    Find all words that are at most 9 letters long and contain every vowel (a, e, i, o, u) in any order.
    :param dictionary:
    :return:
    """
    return re.findall(r'\b((?=.*a.*)(?=.*e.*)(?=.*i.*)(?=.*o.*)(?=.*u.*).{1,9})\b', dictionary)

print(all_vowels_words(dictionary))

print('\nUnique Letter')
def unique_letters(dictionary):
    """
    Find all words that are 10 letters long and do not have any repeating letters.
    :param dictionary:
    :return:
    """
    return [ele.group('letter') for ele in re.finditer(r'\b(?!.*(\w).*\1.*)(?P<letter>.{10})\b', dictionary)]

print(unique_letters(dictionary))

print('\nHTML Encode Ampersands')
def encode_ampersands(text):
    """
    Replace all & characters which are not part of HTML escape sequences by an HTML-encoded ampersand (&amp;).
    :param text:
    :return:
    """
    # print(re.search(r'&(?!.{3};)', text))
    return re.sub(r'&(?!.{3};)', '&amp;', text)

print(encode_ampersands("This &amp; that & that &#38; this."))
# 'This &amp; that &amp; that &#38; this.'
print(encode_ampersands("A&W"))
# 'A&amp;W'

print('\nBroken Markdown Links')
def find_broken_links(text):
    """
    Make a function that accepts a string and returns a list of all reference-style markdown links
    that do not have a corresponding link definition.
    """
    LINK_RE = re.compile(r'''
                         \[
                         (?P<key>.+)
                         \]
                         \[
                         (?P<link>.+)
                         \]
                         (?!(?:.|\n)*\[(?P=link)\])  # 意思是后面不出现相同的link,注意(.|\n)使用,是为了匹配newline和任意字符,因为.不能匹配newline
                        ''', re.VERBOSE|re.IGNORECASE)
    return LINK_RE.findall(text)

print(find_broken_links(r"""
[working link][Google]
    [broken link][baidu]
[working link][Python]
  [google]: www.google.com
[python]: https://www.python.org/"""))
# [('broken link', 'baidu')]


def new_find_broken_links(text):
    LINK_RE = re.compile(r'''
                         \[
                         (?P<link>.+)
                         \]
                         \[
                         (?P<url>.*)
                         \]
                         (?!(?:.|\n)*\[(?P=link)\])  # 意思是后面不出现相同的link,注意(.|\n)使用,是为了匹配newline和任意字符,因为.不能匹配newline
                        ''', re.VERBOSE|re.IGNORECASE)
    return [('broken link', ele.group('link')) for ele in LINK_RE.finditer(text)]



print(new_find_broken_links("""
[Python][]
 [Google][]
 [python]: https://www.python.org/"""))
# [('broken link', 'Google')]

print('\nCamel Case to Underscore')
def convert2underscore(string):
    return re.sub(r'([A-Z])', r'_\1', string).lower()

print(convert2underscore('myCarYourMoney'))

print('\nGet Inline Markdown Links')
def get_inline_links(text):
    """
    Make a function that accepts a string and returns a list of all inline markdown links in the given string.
    """
    LINK_RE = re.compile(r'''
                      \[
                      (?P<language>.+)
                      \]
                      \(
                      (?P<link>.+)
                      \)
                      ''', re.VERBOSE|re.IGNORECASE)
    print(LINK_RE.search(text))
    return [(ele.group('language'), ele.group('link')) for ele in LINK_RE.finditer(text)]

print(get_inline_links("""
[Python](https://www.python.org)
[Google](https://www.google.com)"""))
# [('Python', 'https://www.python.org'), ('Google', 'https://www.google.com')]

print('\nGet All Markdown Links')
def new_get_inline_links(text):
    # 不会...感觉有些难
    pass

get_inline_links("""
[Python](https://www.python.org)
[Google][]
[Another link][example]
[google]: https://www.google.com
[example]: http://example.com""")
# [('Python', 'https://www.python.org'), ('Google', 'https://www.google.com'), ('Another link', 'http://example.com')]