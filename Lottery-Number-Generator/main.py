#
# Haydin Davis
# 10/24
# Lottery Number Generator Programming Project
# COSC 2409 DNT
#
MAX=7
START=0
END=9

def main():
    numbers=[0]*7

    for index in range(MAX):
        numbers[index]= random.randint(START,END)

    print("Here are your lottery numbers:")
    for index in range(MAX):
        print(numbers[index], end='')
    print()

main()
