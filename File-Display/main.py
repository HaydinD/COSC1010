#
# Haydin Davis
# 10/17
# File Display Programming Project
# COSC 2409 DNT
#
myfile=open('numbesr.txt','r')

for line in myfile:
    number=int(line)
    print(number)

myfile.close()
