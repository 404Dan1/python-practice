# CALORIES FROM FAT AND CARBOHYDRATES

# A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation,
#   she asks members for the number of fat grams and carbohydrate grams that they consumed in a day.
#   Then, she calculates the number of calories that result from the fat, using the following formula:
#     + calories from fat = fat grams * 9
# Next, she calculates the number of calories that result from the carbohydrates, using the following formula:
#     + calories from carbs = carb grams * 4
# The nutritionist asks you to write a program that will make these calculations. The program should have
#   a function that accepts fat grams as an argument, and returns the number of calories that result from those
#   fat grams. The program should have another function that accepts carb grams as an argument, and returns the
#   number of calories that result from those carb grams.


def caloric_intake():
  print("RECOMMENDED: it is healthy to consume 44g - 77g of fat per day for daily life.")
  print("Athletes should consume 1.2 - 1.4 g/kg of fat per day")
  print("*"*60)
  fat_grams = int(input("How much fat in grams did you consumed today?: "))
  print("RECOMMENDED: it is healthy to consume 225g - 325g of carbs per day for daily life.")
  print("Athletes should consume 3 - 5 g/kg of carbs per day")
  print("*"*60)
  carb_grams = int(input("How much carbs in grams did you consumed today?: "))

  def calories():
    calories_from_fat = (fat_grams * 9)
    calories_from_carbs = (carb_grams * 4)

    def display_calories():
      print("-"*60)
      print(f"You ate {calories_from_fat} calories from fats today")
      print(f"You ate {calories_from_carbs} calories from carbs today")
      print("-"*60)

    display_calories()

  calories()

caloric_intake()
