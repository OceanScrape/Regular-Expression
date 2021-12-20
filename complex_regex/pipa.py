import re

'''
mencocokan beberapa grup dengan simbol | atau pipa
'''
regex_hero = re.compile(r'Iron Man|Captain America')
mencocokan_objek = regex_hero.search('Iron Man dan Captain America')
grup1 = mencocokan_objek.group() # Iron Man

# frasa
iron_regex = re.compile(r'Iron (man|combat|smith)')
mencocokan_objek1 = iron_regex.search('Iron combat adalah rambo')
grup2 = mencocokan_objek1.group() # pakai parameter 1 hasilnya combat
print(grup2) # Iron combat

