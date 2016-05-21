import re


# Decimal Numbers

def is_number(num_string):
    return bool(re.search(r'^[-+]?(\*\.?\d+|\d+\.)$', num_string))


# Hex Colors

def is_hex_color(string):
    return bool(re.search(r'^#([\da-f]{3}){1,2}$', string, re.IGNORECASE))

def is_hex_color(string):
    return bool(re.search(r'^#[\da-f]{3}([\da-f]{3})?$', string, re.IGNORECASE))

def is_hex_color(string):
    return bool(re.search(r'^#([\da-f]{3}|[\da-f]{6})$', string, re.IGNORECASE))


# Palindromes

[m.group(0) for m in re.finditer(r'\b(.)(.).\2\1\b', dictionary)]


# Double Double

[m.group(0) for m in re.finditer(r'\b.*(.)\1.\1\1.*\b', dictionary)]


# Repetitive Words

[m.group(0) for m in re.finditer(r'\b(.)(.)\1\2\b', dictionary)]


# Get File Extension

# Works with examples given

def get_extension(filename):
    return re.search(r'([^.]*)$', filename).group()

# Works with no extension

def get_extension(filename):
    match = re.search(r'\.([^.]*)$', filename)
    return match.group(1) if match else ''

# Works with only word-based extensions (try ``a.b/c``)

def get_extension(filename):
    match = re.search(r'\.(?!.*\W)([^.]*)$', filename)
    return match.group(1) if match else ''


# Normalize JPEG Extension

def normalize_jpeg(filename):
    return re.sub(r'\.jpe?g$', r'.jpg', filename, flags=re.IGNORECASE)


# Normalize Whitespace

def normalize_whitespace(string):
    return re.sub(r'\s+', r' ', string)


# Compress blank links

def compress_blank_lines(string, max_blanks):
    regex = r'\n{{{n},}}'.format(n=max_blanks)
    return re.sub(regex, '\n' * max_blanks, string)


# Normalize URL

def normalize_domain(url):
    return re.sub(r'^https?://(www.)?treyhunner.com', r'https://treyhunner.com', url)


# Linebreaks

def convert_linebreaks(string):
    string = re.sub(r'\n{2,}', '</p><p>', string)
    string = re.sub(r'\n', '<br>', string)
    return '<p>{}</p>'.format(string)

def convert_linebreaks(string):
    return ''.join(
        '<p>{}</p>'.format(p)
        for p in re.split(r'\n{2,}', string)
    ).replace('\n', '<br>')


# All Vowels

re.findall(r'\b(?=.*a)(?=.*e)(?=.*i)(?=.*o)(?=.*u).{1,9}\b', dictionary)


# Unique Letters

[m.group(0) for m in re.finditer(r'\b(?!.*(.).*\1).{10}\b', dictionary)]


# HTML Encode Ampersands

def encode_ampersands(string):
    return re.sub(r'&(?![#\w]+;)', '&amp;', string)


# Broken Markdown Links

# With verbose regular expression

def find_broken_links(string):
    BROKEN_LINKS_RE = re.compile(r'''
        \[ (?P<text> .*?) \]
        \[ (?P<ref> .+?) \]
        (?!
            [\s\S]+
            \[ (?P=ref) \]: \s+
        )
    ''', re.VERBOSE | re.IGNORECASE)
    return [
        (m.group('text'), m.group('ref'))
        for m in BROKEN_LINKS_RE.finditer(string)
    ]

# Supporting implicit link names

BROKEN_RE1 = re.compile(r'''
    \[ (?P<text> .*?) \]
    \[ (?P<ref> .+?) \]
    (?!
        [\s\S]+
        \[ (?P=ref) \]: \s+
    )
''', re.VERBOSE | re.IGNORECASE)
BROKEN_RE2 = re.compile(r'''
    \[ (?P<ref> (?P<text> .+?)) \]
    \[ \]
    (?!
        [\s\S]+
        \[ (?P=text) \]: \s+
    )
''', re.VERBOSE | re.IGNORECASE)

def find_broken_links(string):
    return [
        (m.group('text'), m.group('ref'))
        for regex in (BROKEN_RE1, BROKEN_RE2)
        for m in regex.finditer(string)
    ]


# Camel Case to Underscore

# This acts strangely with ``HTTPResponse``

def camel_to_underscore(string):
    return re.sub(r'(.)([A-Z])', r'\1_\2', string).lower()

# This turns ``HTTPResponse`` into ``httpresponse``

def camel_to_underscore(string):
    return re.sub(r'(?<=[a-z])([A-Z])', r'_\1', string).lower()

# This turns ``HTTPResponse`` into ``http_response``

def camel_to_underscore(string):
    return re.sub(r'(?<=.)([A-Z])(?=[^A-Z])', r'_\1', string).lower()


# Get Inline Markdown Links

INLINE_RE = re.compile(r'''
    \[ (?P<text> .*?) \]
    \( (?P<url> .+?) \)
''', re.VERBOSE)


def get_inline_links(string):
    return [
        (m.group('text'), m.group('url'))
        for m in INLINE_RE.finditer(string)
    ]


# Get All Markdown Links

REF1_RE = re.compile(r'''
    \[ (?P<text> .*?) \]
    \[ (?P<ref> .+?) \]
    (?=
        [\s\S]+
        \[ (?P=ref) \]: \s+
        (?P<url> .+)
    )
''', re.VERBOSE | re.IGNORECASE)
REF2_RE = re.compile(r'''
    \[ (?P<text> .*?) \]
    \[\]
    (?=
        [\s\S]+
        \[ (?P=text) \]: \s+
        (?P<url> .+)
    )
''', re.VERBOSE | re.IGNORECASE)
INLINE_RE = re.compile(r'''
    \[ (?P<text> .*?) \]
    \( (?P<url> .+?) \)
''', re.VERBOSE)


def get_markdown_links(string):
    results = (
        r.finditer(string)
        for r in (INLINE_RE, REF1_RE, REF2_RE)
    )
    return [
        (m.group('text'), m.group('url'))
        for matches in results
        for m in matches
    ]