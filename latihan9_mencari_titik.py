import re

'''
mencari karakter . menggunakan backslah \
karakter . dibawah bukan metakarakter, melainkan ingin mencocokan dengan karakter .
'''
kalimat = 'this is ok.'
pola = re.search(r'\.', kalimat)
print(pola) # <re.Match object; span=(10, 11), match='.'>