import re

'''
re.sub ==> subtitution
'''

kata = 'In 1908, Budi Utomo was formed. The Youth Pledge was declared in 1928.' \
       ' Indonesia declared independence in 1945'
print(re.sub('\d{4}', 'YEAR', kata)) # In YEAR, Budi Utomo was formed. The Youth Pledge was declared in YEAR. Indonesia declared independence in YEAR