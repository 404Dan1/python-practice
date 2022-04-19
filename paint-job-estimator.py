# PAINT JOB ESTIMATOR

# A painting company has determined that for every 112 square feet of wall space, one gallon of paint and
#   eight hours of labor will be required. The company charges $35.00 per hour for labor. Write a program
#   that asks the user to enter the square feet of wall space to be painted and the price of the paint per
#   gallon. The program should display the following data:
#     + The number of gallons of paint required
#     + The hours of labor required
#     + The cost of the paint
#     + The labor charges
#     + The total cost of the paint job


def estimator():
  area = float(input("How much sq.ft you want to cover?: "))
  print("NOTE: Low grade paint cost around $15 per gallon and some high grade cost around $30-$40 per gallon")
  paint_price = float(input("What is the price of your paint?: "))

  def calculations():
    gallon_paint = (area / 112)
    labor_hours = (area / 112 * 8)
    cost_paint = (area / 112 * paint_price)
    charges = (area / 112 * 35)
    total_cost = (cost_paint + charges)

    def display():
      print("*"*60)
      print(f"You would need {gallon_paint:.1f} gallons of paint")
      print(f"This amounts to {labor_hours:.0f} hours of work")
      print(f"If the paint cost {paint_price:.0f} dollars per gallon then total cost is ${cost_paint:.2f}")
      print(f"If it takes {labor_hours:.0f} hours of work then the total cost is ${charges:.2f}")
      print(f"The total price of the job is ${total_cost:.2f}")
      print("*"*60)

    display()

  calculations()

estimator()
