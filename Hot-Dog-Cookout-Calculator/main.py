#
# Haydin Davis
# 9/16
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
HOT_DOGS_PER_PACK=10
BUNS_PER_PACK=8
#Ask for the amount of people
people=int(input('How many people are going to be at the cookout?(whole number): '))
dogsPerPerson=int(input('How many hot dogs would each person like?(whole number: )'))
#Divide the people by the amount in packs
amountofDogs=people*dogsPerPerson
minHotDogs=int(amountofDogs/HOT_DOGS_PER_PACK)
minBuns=int(amountofDogs/BUNS_PER_PACK)
leftoverDogs=amountofDogs%HOT_DOGS_PER_PACK
leftoverBuns=amountofDogs%BUNS_PER_PACK
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
