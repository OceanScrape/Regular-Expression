import re

'''
\d\d\d mencari tiga angka secara berurutan
bisa juga diganti dengan \d{3}
'''
kata = 'bla456bla'
pola = re.search(r'\d\d\d', kata)
print(pola) # <re.Match object; span=(3, 6), match='456'>

