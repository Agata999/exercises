import math

argument_list = []
for i in range(100):
    argument_list.append(i/10)

formula = input("Please enter a formula, use 'x' as the argument: ")

for x in argument_list:
    print(f'For x = {x} the result of your formula is {eval(formula) :2.2f}')
