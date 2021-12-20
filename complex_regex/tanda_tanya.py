import re

'''
latihan question mark
()?
muncul 0 sampai satu
'''

iron_regex = re.compile(r'Iron (wo)?man')
mencocokan_objek = iron_regex.search('Petualangan Iron woman')
grup1 = mencocokan_objek.group()
print(grup1) # Iron woman

# Nomor telfon

regex_telfon = re.compile(r'(\d{3}-)?\d{3}-\d{3}-\d{3}')
mencocokan_objek1 = regex_telfon.search('nomor telfon saya 456-789-012')
cetak = mencocokan_objek1.group()
print(cetak) # 456-789-012
