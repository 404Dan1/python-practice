# AVERAGE STEPS TAKEN
# A personal Fitness Tracker is a wearable device that tracks your physical activity, calories burned,
#   heart rate, sleeping patterns, and so on. One common physical activity the most of these devices track
#   is the number of steps you take each day.

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months = [
  "January", 
  "February", 
  "March", 
  "April", 
  "May", 
  "June", 
  "July", 
  "August", 
  "September", 
  "October", 
  "November", 
  "December"
]

first_month = 0

last_month = 0

open_file = open("steps.txt", "r")
output_file = open("King_avg.txt", "w")
output_file.write("These are the averages of the steps I've taken each month\n")
output_file.write("Month | Avg\n")
print("Month | Avg\n")
month_lines = open_file.readlines()
month_lines = list(map(int, month_lines))

for month in range(0,12):
  last_month = first_month + month_days[month]
  monthLines = month_lines[first_month:last_month]
  average = float(sum(monthLines))/ max(len(monthLines), 1)
  output_file.write(f"{months[month]} | {average:.0f}\n")
  print(f"{months[month]} | {average:.0f}\n")
  first_month = last_month

open_file.close()
output_file.close()
