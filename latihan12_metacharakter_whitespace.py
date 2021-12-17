import re

'''
\s mencocokan spasi
perlu diingat bahwa metode search hanya akan mengembalikan hasil pencocokan pertama
'''

kata = 'bla 123 bla'
pola = re.search(r'\s', kata)
print(pola) # <re.Match object; span=(3, 4), match=' '>