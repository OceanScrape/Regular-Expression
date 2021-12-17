import re
'''
pola hanya mencari '456' saja, jika ada berarti mactch
'''
kata = r'bla456blaa'
pola = re.search(r'456', kata)
print(type(pola)) # <class 're.Match'> tipe
print(pola) # <re.Match object; span=(3, 6), match='456'> ekslusif
print(kata[3:6]) # 456 slicing
