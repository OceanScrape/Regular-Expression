import re

'''
^ awal dari kata
^ diluar kurung siku menandakan metakarakter start
^ didalam kurung siku menandakan negasi
^[A-z] konteksnya sebagai awal dari kata
jika kata pertama ada angka hasilnya None
'''

kata = 'Insonesia Raya'
pola = re.search(r'^[A-z]', kata)
print(pola) # <re.Match object; span=(0, 1), match='I'>