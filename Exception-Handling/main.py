#
# Haydin Davis
# 10/24
# Exeptional Handling
# COSC 2409 DNT
#

def main():
    try:
        total=0
        infile=open('number.txt','r')
        lines=0
        contents=lines.readline()

        while contents != "":
            lines+=1
            total+=int(contents)
            contents=lines.readline()
        
        average=total/lines
    except IOError:
        print("An IOError ocurred")
    except ValueError:
        print("A ValueError ocurred")
    else:
        print("average is", average)
main()
