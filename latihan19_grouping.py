import re

'''
grouping ()
cat+ vs (cat)+
'''

kata1 = 'cattt'
kata2 = 'catcatcat'
print(re.search('cat+', kata1)) # <re.Match object; span=(0, 5), match='cattt'>
print(re.search('cat+', kata2)) # <re.Match object; span=(0, 3), match='cat'>
print(re.search('(cat)+', kata1)) # <re.Match object; span=(0, 3), match='cat'>
print(re.search('(cat)+', kata2)) # <re.Match object; span=(0, 9), match='catcatcat'>
