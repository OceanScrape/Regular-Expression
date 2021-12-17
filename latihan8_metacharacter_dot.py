import re

'''
metakarakter . akan cocok/match dengan semua karakter kecuali
new line
.. akan cocok dengan semua karakter kecuali new line
'''
kata = 'bl!3BM'
pola = re.search('.[0-9]..', kata)
print(pola) # <re.Match object; span=(0, 4), match='!3BM'>