#price of each item purchased

item1 = float(input('Enter the price of the first item '))
item2 = float(input('Enter the price of the second item '))
item3 = float(input('Enter the price of the third item '))
item4 = float(input('Enter the price of the fourth item '))
item5 = float(input('Enter the price of the fith item '))

#getting the subtotal
subtotal = (item1 + item2+ item3+ item4+ item5)

#get the sales tax
sales_tax = (subtotal * .07)

#get the total of sale k
total = (subtotal + sales_tax)

#display the subtotal, sales tax and total
print('The subtotal is', subtotal)
print(f'The sales tax is, ${sales_tax:,.2f}')
print(f'The total is, ${total:,.2f}')




