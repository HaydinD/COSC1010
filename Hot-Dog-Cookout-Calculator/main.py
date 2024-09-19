#
# Haydin Davis
# 9/16
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
#Ask for the amount of people
people=int(input('How many people are going to be at the cookout?(whole number): '))
dogsPerPerson=int(input('How many hot dogs would each person like?(whole number: )'))
#Divide the people by the amount in packs
amountofDogs=people*dogsPerPerson
minHotDogs=int(amountofDogs/10)
minBuns=int(amountofDogs/8)
leftoverDogs=amountofDogs%10
leftoverBuns=amountofDogs%8
# Use comments liberally throughout the program. 
if leftoverDogs==0:
    print('You will need ', minHotDogs,'packs of hot dogs.')
else:
    print('You will need ', minHotDogs+1,'packs of hot dogs.')

if leftoverBuns==0:
    print('You will need ', minBuns,'packs of buns.')
else:
    print('You will need ', minBuns+1,'packs of buns.')

print('You will have ', leftoverDogs,'hot dogs left over.')
print('You will have ', leftoverBuns,'buns left over.')
