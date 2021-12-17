import re

'''
$ kebalikan dari ^
[A-z][A-z]$ apakah diakhiri dengan 2 huruf
'''

kata = '1945 Indonesia Raya'
pola = re.search(r'[A-z][A-z]$', kata)
print(pola) # <re.Match object; span=(18, 19), match='ya'>