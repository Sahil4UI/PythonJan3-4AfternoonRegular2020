Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #slicing
>>> x= "hello everyone how are you????"
>>> x[0:5]
'hello'
>>> x[:5]
'hello'
>>> x[5:]
' everyone how are you????'
>>> x[:]
'hello everyone how are you????'
>>> #slicing[starting index:ending index:stepsize(Inc/Dec)]
>>> x[0:5]
'hello'
>>> x[0:5:1]
'hello'
>>> x[0:5:2]
'hlo'
>>> #find the reverse of String
>>> x = "shyam" #mayhs
>>> x[-1:5]
'm'
>>> x[-1:]
'm'
>>> x[-1:-5]
''
>>> x[-1:-6:-1]
'mayhs'
>>> x[-1::-1]
'mayhs'
>>> x[::-1]
'mayhs'
>>> #methods in String
>>> x
'shyam'
>>> x.upper()
'SHYAM'
>>> x
'shyam'
>>> x = x.upper()
>>> x
'SHYAM'
>>> x.lower()
'shyam'
>>> x
'SHYAM'
>>> #string->immutable->which cannot be changed
>>> x.casefold()#lower
'shyam'
>>> x = "pYtHoN"
>>> x.swapcase()
'PyThOn'
>>> x
'pYtHoN'
>>> x.replace('p','z')
'zYtHoN'
>>> x = 'aabbcccddeeeaaaaaa'
>>> x.replace('a','Y')
'YYbbcccddeeeYYYYYY'
>>> x.replace('a','Y',1)
'Yabbcccddeeeaaaaaa'
>>> x.replace('a','Y',3)
'YYbbcccddeeeYaaaaa'
>>> x
'aabbcccddeeeaaaaaa'
>>> x = "python is a HLL"
>>> x.replace('python','JS')
'JS is a HLL'
>>> x
'python is a HLL'
>>> x.index('p')
0
>>> x = 'abcdabcd'
>>> x.index('a')
0
>>> x.index('a',0)
0
>>> x.index('a',1)
4
>>> x.find('a')
0
>>> x.find('a',1)
4
>>> x.rfind('a')
4
>>> x.index('X')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x.index('X')
ValueError: substring not found
>>> x.find('X')
-1
>>> #-1 - substring not found
>>> x = "Welcome to python programming class"
>>> x.split()
['Welcome', 'to', 'python', 'programming', 'class']
>>> l = x.split()
>>> l
['Welcome', 'to', 'python', 'programming', 'class']
>>> l[0]
'Welcome'
>>> l[1]
'to'
>>> l[-1]
'class'
>>> len(l)
5
>>> x
'Welcome to python programming class'
>>> x.split('o')
['Welc', 'me t', ' pyth', 'n pr', 'gramming class']
>>> x = 'Hey!!'
>>> x.center(2)
'Hey!!'
>>> x.center(3)
'Hey!!'
>>> x.center(5)
'Hey!!'
>>> x.center(6)
'Hey!! '
>>> x.center(13)
'    Hey!!    '
>>> x.center(13,'*')
'****Hey!!****'
>>> x.center(13,'-')
'----Hey!!----'
>>> x.center(13,'\n')
'\n\n\n\nHey!!\n\n\n\n'
>>> x = x.center(30,'*')
>>> x
'************Hey!!*************'
>>> x.replace('*',' ')
'            Hey!!             '
>>> x.replace('*','')
'Hey!!'
>>> x.strip('*')
'Hey!!'
>>> x
'************Hey!!*************'
>>> x.lstrip('*')
'Hey!!*************'
>>> x.rstrip('*')
'************Hey!!'
>>> x = "python".center(20)
>>> x
'       python       '
>>> x.strip()
'python'
>>> x.lstrip()
'python       '
>>> x.rstrip()
'       python'
>>> x
'       python       '
>>> x = x.strip()
>>> x
'python'
>>> x.zfill(30)
'000000000000000000000000python'
>>> x
'python'
>>> x.isalpha()
True
>>> x = "abc123"
>>> x.isalpha()
False
>>> x.isalnum()
True
>>> x = '12323453'
>>> x.isdigit()
True
>>> #ASCII(American standard code for information interchange) VALUE CHART
>>> # ord()-ordinal function & chr()-character
>>> ord('A')
65
>>> ord('@')
64
>>> chr(112)
'p'
>>> chr('a')
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    chr('a')
TypeError: an integer is required (got type str)
>>> chr(97)
'a'
>>> x='हेलो क्या हाल है?'
>>> x
'हेलो क्या हाल है?'
>>> x.encode()
b'\xe0\xa4\xb9\xe0\xa5\x87\xe0\xa4\xb2\xe0\xa5\x8b \xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe \xe0\xa4\xb9\xe0\xa4\xbe\xe0\xa4\xb2 \xe0\xa4\xb9\xe0\xa5\x88?'
>>> x.decode()
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    x.decode()
AttributeError: 'str' object has no attribute 'decode'
>>> x
'हेलो क्या हाल है?'
>>> x=x.encode()
>>> x
b'\xe0\xa4\xb9\xe0\xa5\x87\xe0\xa4\xb2\xe0\xa5\x8b \xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe \xe0\xa4\xb9\xe0\xa4\xbe\xe0\xa4\xb2 \xe0\xa4\xb9\xe0\xa5\x88?'
>>> x.decode()
'हेलो क्या हाल है?'
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
 |      such as "def" or "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  removeprefix(self, prefix, /)
 |      Return a str with the given prefix string removed if present.
 |      
 |      If the string starts with the prefix string, return string[len(prefix):].
 |      Otherwise, return a copy of the original string.
 |  
 |  removesuffix(self, suffix, /)
 |      Return a str with the given suffix string removed if present.
 |      
 |      If the string ends with the suffix string and that suffix is not empty,
 |      return string[:-len(suffix)]. Otherwise, return a copy of the original
 |      string.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(...)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> x= "hello"
>>> y = "python"
>>> x+y
'hellopython'
>>> x-y
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    x-y
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> x*z
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    x*z
NameError: name 'z' is not defined
>>> x/y
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    x/y
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> 'hi'*10
'hihihihihihihihihihi'
>>> x = "unsupported operand type(s) for /: 'str' and 'str'"
>>> x.capitalize()
"Unsupported operand type(s) for /: 'str' and 'str'"
>>> x.title()
"Unsupported Operand Type(S) For /: 'Str' And 'Str'"
>>> x
"unsupported operand type(s) for /: 'str' and 'str'"
>>> x.startswith('x')
False
>>> x.startswith('u')
True
>>> x.endswith("'")
True
>>> #in operator
>>> 'a' in x
True
>>> 