#
# Haydin Davis
# 9/5/24
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations

# Constants for the state and county tax rates

# Get the amount of the purchase.
purchase=float(input('Enter Project Sales: '))
# Calculate the state sales tax.
tax1=purchase*0.05
# Calculate the county sales tax.
tax2=purchase*0.025
# Calculate the total tax.
tax=tax1+tax2
# Calculate the total of the sale.
total=tax+purchase
# Print information about the sale.
print('The purchase is $', format(purchase,',.2f'))
print('The state tax is $', format(tax1,',.2f'))
print('The county tax is $', format(tax2,',.2f'))
print('The total tax is $', format(tax,',.2f'))
print('The total is $', format(total,',.2f'))
