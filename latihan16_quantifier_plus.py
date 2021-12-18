import re

'''
quntifier +
minimal match SATU atau lebih !0

'''

kata1 = 'ct'
kata2 = 'cat'
kata3 = 'caaaaat'
print(re.search('ca+t', kata1)) # None
print(re.search('ca+t', kata2)) # <re.Match object; span=(0, 3), match='cat'>
print(re.search('ca+t', kata3)) # <re.Match object; span=(0, 7), match='caaaaat'>