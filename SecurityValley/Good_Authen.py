s1 = 'sont'
s2 = 'TbxT'
s3 = 'jffe'

for i in s1:
    print(chr((ord(i)^7)),end='')
for i in s2:
    print(chr((ord(i)^11)),end='')
for i in s3:
    print(chr((ord(i)^9)),end='')

# this_is_cool