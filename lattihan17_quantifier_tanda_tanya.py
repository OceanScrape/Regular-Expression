import re

'''
quantifier ?
minimal cocok/match NOL atau SATU
'''
kata1 = 'color'
kata2 = 'colour'
kata3 = 'colouur' # hasil None karena u muncul sebanyak DUA kali

print(re.search('colou?r', kata1)) # <re.Match object; span=(0, 5), match='color'>
print(re.search('colou?r', kata2)) # <re.Match object; span=(0, 6), match='colour'>
print(re.search('colou?r', kata3)) # None
