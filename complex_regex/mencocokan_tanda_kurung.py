import re

'''
mencocokan (012)
deteksi berbagai karakter :
\. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)
'''

regex_nomor_telfon = re.compile(r'(\(\d{3}\)) (\d{3}-\d{3}-\d{4})')
mencocokan_objek = regex_nomor_telfon.search('Nomor telfon saya adalah (012) 345-678-9012')
grub1 = mencocokan_objek.group(1)
print(grub1) # (012)
