import re

'''
metakarakter \w akan cocok/match dengan alphanumeric [a-zA_Z0-9_]
underscore juga termasuk
\w\w\w\w' mencari alpanumerik secara berurutan (ada 4)
bisa juga diganti dengan \w{4}
'''
kata = '@93 CbA_ ikkkp'
pola = re.search(r'\w\w\w\w', kata)
print(pola) # <re.Match object; span=(4, 8), match='CbA_'>