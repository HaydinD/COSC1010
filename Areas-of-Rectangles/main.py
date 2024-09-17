#
# Haydin
# 9/16
# Areas of Rectangles Programming Project
# COSC 2409 DNT
#
# Local variables

# Get length A
lengthA=float(input('Enter a length for Rectangle A: '))
# Get width A
widthA=float(input('Enter a width for Rectangle A: '))
# Get length B
lengthB=float(input('Enter a length for Rectangle B: '))
# Get width B
widthB=float(input('Enter a width for Rectangle B: '))
# Calculate area A
areaA=lengthA*widthA
# Calculate area B
areaB=lengthB*widthB
# Print area comparison using if-elif-else statements
if areaA>areaB:
    print('Rectangle A has a greater area.')
elif areaB>areaA:
    print('Rectangle B has a greater area.')
else:
        print('They both have the same area.')
