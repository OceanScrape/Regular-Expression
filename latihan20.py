import re

'''
kata1 ==> feb(ruary)? ==> boleh muncul 0 atau satu kali
kata2 ==> feb(ruary)? tentu saja cocok
kata3 ==> feb(ruary)? ==> feby nya sudah tidak cocok
'''
kata1 = 'Feb 2022'
kata2 = 'February 2022'
kata3 = 'Feby 2022'

print(re.search('Feb(ruary)? 2022', kata1)) # <re.Match object; span=(0, 8), match='Feb 2022'>
print(re.search('Feb(ruary)? 2022', kata2)) # <re.Match object; span=(0, 13), match='February 2022'>
print(re.search('Feb(ruary)? 2022', kata3)) # None