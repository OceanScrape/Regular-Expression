import re

'''
gr[ae]y
gr boleh diikuti antara a atau e dan diikuti dengan y
'''
kata = 'the color is grey'
pola = re.search(r'gr[ae]y', kata)
print(pola) # <re.Match object; span=(13, 17), match='grey'>