import re

'''
mencari nomor telfon dengan fungsi re.compile
untuk memastikan kunjungi pythex.org
'''

regex_nomor_telfon = re.compile(r'\d{3}-\d{3}-\d{3}-\d{4}')
mencocokan_objek = regex_nomor_telfon.search('Nomor telfon saya adalah 012-345-678-9012')
print('Nomor telfon ditemukan: ' + mencocokan_objek.group())
# Nomor telfon ditemukan: 012-345-678-9012