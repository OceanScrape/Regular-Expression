import re

'''
Negasi artinya selain dari
Negasi ditulis dengan ^
Negasi harus ditulis diDALAM kurung siku
pola [^0-9A-z] akan cocok/ match dengan karakter selain itu
'''

kata = 'bla3B1!!aa'
pola = re.search(r'[^0-9A-z][^0-9A-z][0-9A-z]', kata)
print(pola) # <re.Match object; span=(6, 9), match='!!a'>