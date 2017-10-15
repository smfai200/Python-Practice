from __future__ import print_function
import os
#Insert in List
list = ["FAIZAN", "JALAL", "SALMAN", "KONI"]

name = raw_input("NAME: ")
name1 = name.upper()

list.append(name1)
for x in range(0,len(list)):
    print(list[x], end="  ")


