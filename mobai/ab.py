
from difflib import SequenceMatcher
a = raw_input()
b = raw_input()

a = 'abe'
b = 'cabcccc'

match = SequenceMatcher(None, a, b).find_longest_match(0, len(a), 0, len(b))
out = min(len(a) - match[2], len(a))

print out


