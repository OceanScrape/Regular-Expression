import re

'''
Memisahkan per grup dengan tanda kurung ()
group() dan group(0) outputnya sama
jika ingin semua grup dijadikan satu gunakan groups()
output dari groups() merupakan tipe data tuple
'''

regex_nomor_telfon = re.compile(r'(\d{3}-\d{3})-(\d{3}-\d{4})')
mencocokan_objek = regex_nomor_telfon.search('Nomor telfon saya adalah 012-345-678-9012')
grub1 = mencocokan_objek.group(1)
grub2 = mencocokan_objek.group(2)
allgrub = mencocokan_objek.groups()
kode_area, nomer_utama = mencocokan_objek.groups()
print(grub1) # 012-345
print(grub2) # 678-9012
print(allgrub) # ('012-345', '678-9012')


