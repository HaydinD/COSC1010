#
# Haydin Davis
# 10/17
# Average of Numbers
# COSC 2409 DNT
#

def main():
    total=0
    infile=open('number.txt','r')
    lines=0
    contents=lines.readline()

    while contents != "":
        lines+=1
        total+=int(contents)
        contents=lines.readline()
    
    average=total/lines
    print("average is", average)
main()
