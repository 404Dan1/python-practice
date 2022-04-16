# SUM OF DIGITS IN A STRING

# Write a program that asks the user to enter a series of single-digit numbers with nothing separating them.
# The program should display the sum of all the single digit numbers in the string. 
# For example, if the user enters 2514, the method should return 12, which is the sum of 2, 5, 1 and 4






def digit_numbers():
    # takes the user input
    user_input = input('Enter several series of numbers: ')

    def calculations(string):
        # calculates the user input
        total = 0
        count = 0

        for i in range(len(string)):
            count = int(string[i])
            total += count

        return total

    def display():
        # displays the user input and the total of the input
        dig_num = calculations(user_input)

        print(f'You entered {user_input}')
        print('*' * 25)
        print(f'The total of the numbers entered: {dig_num}')

    display()


digit_numbers()
