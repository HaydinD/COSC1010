#
# Haydin Davis
# 9/24
# Feet to Inches Programming Project
# COSC 2409 DNT
IN_PER_FT=12

def main():
    feet=int(input('Enter a number of feet: '))
    print(feet, 'equals', ft_to_in(feet),'inches.')

def ft_to_in(feet):
    return feet*IN_PER_FT

main()
