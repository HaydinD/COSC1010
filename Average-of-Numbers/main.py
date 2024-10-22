#
# Haydin Davis
# 10/17
# Average of Numbers Programming Project
# COSC 2409 DNT
#
def main():
    contents=''
    infile=open('number.txt','r')
    contents=infile.read()
    average=contents/3
    print(average)
main()
