import re

'''
{m,n} jumlah minimal m dan maksimal n
{m} harus tepat sejumlah m
colo{2,4}r ==> apakah o match sebanyak minimal 2 maksimal 4 pada kata1
'''

kata1 = 'coloor'
kata2 = 'coloooor'
kata3 = 'color'
print(re.search('colo{2,4}r', kata1)) # <re.Match object; span=(0, 6), match='coloor'>
print(re.search('colo{2,4}r', kata2)) # <re.Match object; span=(0, 8), match='coloooor'>
print(re.search('colo{2,4}r', kata3)) # None
print(re.search('colo{2}r', kata1)) # <re.Match object; span=(0, 6), match='coloor'>