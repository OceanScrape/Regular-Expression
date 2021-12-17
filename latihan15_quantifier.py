import re

'''
regex quantifier * atau axterisk
bisa muncul 0 kali atau lebih

ca*t ==> a boleh muncul 0 kali atau lebih, program tidak error jika a tidak ada
'''

kata1 = 'ct'
kata2 = 'cat'
kata3 = 'caaaaat'
print(re.search('ca*t', kata1)) # <re.Match object; span=(0, 2), match='ct'>
print(re.search('ca*t', kata2)) # <re.Match object; span=(0, 3), match='cat'>
print(re.search('ca*t', kata3)) # <re.Match object; span=(0, 7), match='caaaaat'>