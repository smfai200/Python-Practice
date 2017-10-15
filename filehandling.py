import os

f = open('abc.txt','w')
f.write("THIS IS APPENDED LINE-1\n")
f.write("THIS IS SECOND APPENDED LINE!\n")
f.write("HEY ITS WORKING!!!\n")
f.close();

f1 = open('abc.txt','r')
for line in f1:
    print "==> ",line
f1.close();
