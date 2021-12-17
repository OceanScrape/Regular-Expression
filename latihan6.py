import re

'''
[A-z] ==> huruf besar dan kecil termasuk
'''
kata = 'bla3Bla'
pola = re.search('[A-z][0-9][A-z]', kata)
print(pola) # <re.Match object; span=(2, 5), match='a3B'>
