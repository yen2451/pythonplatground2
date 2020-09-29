# -*- coding=utf-8 -*-
s = input("plz input the source\n")
sb = int(input("the source base is?\n"))
base = input("convert to which base\n")
i = int(s, sb)
if (base == '2'):
    print(bin(i))
elif (base == '8'):
    print(oct(i))
elif (base == '10'):
    print(i)
else:
    print(hex(i))
