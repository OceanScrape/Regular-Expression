import re

'''
Lakukan scaning pada variabel 'kata' yang berisi string dan mencari kemunculan pertama dimana patternya
'456' itu akan mendapat match
'''
kata = 'bla456blaa'
pola = re.search(r'456', kata)
if pola:
    print('Found!')
else:
    print('Not found!')
# Found!

