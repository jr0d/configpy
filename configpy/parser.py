"""
Parsing the data, regex not required.
"""

import os

LIST = '[]'
DICT = '{}'
TUP = '()'

STR_OC = [('\'','\''), ('\"', '\"')]
UNI_OC = [('u\'', '\''), ('u\"', '\"')]
STR_MOC = [('\'\'\'', '\'\'\''), ('\"\"\"', '\"\"\"')]
UNI_MOC = [('u\'\'\'', '\'\'\''), ('u\"\"\"', '\"\"\"')]

LINE_BREAK  = '\\'
MAX_LINE = 2048
MAX_TERM = 256

VALID_CHARS = [chr(x) for x in range(48,122) if chr(x).isalnum()] + ['_']

class ConfigPyParserException(Exception):pass

def validate_name(name_string):
    if not isinstance(name_string, (str, unicode)):
        raise TypeError('Invalid Type: %s' % type(name_string))
    len_str = len(name_string)
    if len_str > MAX_TERM:
        raise ConfigPyParserException('Term is too big: %d' % len_str)
    if not name_string[0].isalpha():
        raise ConfigPyParserException('Term must begin with an alphanumeric '
                                      'character')
    for c in name_string:
        if c not in VALID_CHARS:
            raise ConfigPyParserException('Term cannot contain any special '
                                      'characters or whitespace.')
    return name_string

def is_section_get_section(line):
    """
    line should already be checked against MAX_LINE
    """
    line.strip()
    line_length = len(line)
    if line_length < 3:
        return
    if line[0] != '[' or line[-1] != ']':
        return
    mid = line[1:-1].strip()
    return validate_name(mid)


config = u"""
[Section1]
integer = 1234
string1 = 'I am a string'
string2 = "I am a string 2"
unicode_string1 = u'I am a unicode string'
unicode_string2 = u"I am a unicode string 2"
list1 = [1234, 'String1', u'unicode1', 22.5, string1]
dict1 = {'key1':string2, 'key2': 9876}
tup1 = (1,2,3,string1, 99,  list1)
[Section_2]
multiline_string = "Hello, My name is jared \\
    Rodriguez"
muitline_expresion = ['I am a list element' \\
    'I am a list element on another line']
I should cause an error.
"""

if __name__ == '__main__':
    for line in config.splitlines():
        if len(line) > MAX_LINE:
            raise Exception('The world is going to burn')
        line = line.strip()
        if not line:
            continue

        sec = is_section_get_section(line)
        if not sec:
            continue
        if sec:
            print sec


