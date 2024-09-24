#
# Haydin Davis
# 9/24
# Kilometer Converter Programming Project
# COSC 2409 DNT
CONVERSION_FACTOR=0.6214
# Use comments liberally throughout the program. 
def main():
    kilometers=float(input('Enter a distance in kilometers: '))
    miles(kilometers)
def miles(km):
    miles=km*CONVERSION_FACTOR

    print(km,'kilometers equals',miles,'miles.')

main()
