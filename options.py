options = ['load data', 'export data', 'analyze & predict']


def display_options(options):
    for i in range(len(options)):
        print(f'{i+1} - {options[i]}')
    choice = input('Select option above or press enter to exit: ')
    return choice


choice = 'x'
while choice:
    choice = display_options(options)
    if choice:
        try:
            choice_num = int(choice) - 1
            if 0 <= choice_num < len(options):
                print(f'You chose {choice_num+1} - {options[choice_num]}')
            else:
                print('You have to enter a number from the list')
        except ValueError:
            print('You have to enter a number')
    else:
        print('It\'s the end')



