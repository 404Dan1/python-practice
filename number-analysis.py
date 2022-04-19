
# Design a program that asks the user to enter a series of 20 numbers. The program should store the numbers
#   in a list then display the following data:
#     + The lowest number in the list
#     + The highest number in the list
#     + The total of the numbers in the list
#     + The average of the numbers in the list


import random


def number_analysis():

  numbers_list = []
  for i in range(20):
    numbers_list.append(random.randint(1, 100))

    def display_num():
      print(f"The lowest number in the list is {min(numbers_list)}")
      print(f"The highest number in the list is {max(numbers_list)}")
      print(f"The total of the numbers in the list is {sum(numbers_list)}")
      print(f"The average of the numbers in the list is {sum(numbers_list)/20}")
      print(f"The list of the numbers are {numbers_list}")

  display_num()


number_analysis()
