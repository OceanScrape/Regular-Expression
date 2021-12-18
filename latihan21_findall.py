import re

'''
re.findall
melakukan semua pencarian untuk semua mactching dari polanya
sifatnya overlapping
'''

kata = 'In 1908, Budi Utomo was formed. The Youth Pledge was declared in 1928.' \
       ' Indonesia declared independence in 1945'
print(re.findall('\d{4}', kata)) # ['1998', '1928', '1945']
