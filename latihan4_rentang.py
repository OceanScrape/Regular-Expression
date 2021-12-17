import re
'''
[0-9] rentang 0 sampai 9 akan match
pola regex mencari 3 digit angka
jika pada string hanya terdapat 2 digit angka,
tapi pada pola regex mencari 3 digit, hasilnya None
'''
kata = 'bla456bla'
pola = re.search(r'[0-9][0-9][0-9]', kata) # repetisi
print(pola) # <re.Match object; span=(3, 6), match='456'>
