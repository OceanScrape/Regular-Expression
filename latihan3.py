import re
'''
pola hanya mencari eksklusif '234' saja, kalau tidak match hasilnya 'None'
'''
kata = 'bla456bla'
pola = re.search(r'234', kata)
print(pola) # None
