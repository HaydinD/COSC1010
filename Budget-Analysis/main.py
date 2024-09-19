#
# Haydin Davis
# 9/19
# Budget Analysis Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
budget=float(input('What is your budget for the month: $'))
expenses=0
#This will repeat until you are under budget.
while expenses<=0:
    supplies=float(input('How much do you spend on groceries: $'))
    water=float(input('How much is your water bill: $'))
    electricity=float(input('How much is your electric bill: $'))
    leisure=float(input('How much do you spend on activities: $'))
    hobbies=float(input('How much do you spend on hobbies: $'))
    expenses=budget-supplies-water-electricity-leisure-hobbies
    if expenses>0:
        print('You are under budget.')
    elif expenses<0:
        print('You are over budget.')
        print('Try again.')
    else:
        print('You are at budget.')
        print(input('Try to lower that a little?'))
