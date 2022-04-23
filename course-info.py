# COURSE INFORMATION

# Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where
#   the courses meet. The dictionary should have the following key-value pairs:

#     |Course Number(key)|    |Room Number(value)|
#         CS101                 3004
#         CS102                 4501
#         CS103                 6755
#         NT110                 1244
#         CM241                 1411

# The program should also create a dictionary containing course numbers and the names of the instructors that teach
#   each course. The dictionary should have the following key-value pairs:

#     |Course Number(key)|    |Instructor (value)|
#         CS101                 Haynes
#         CS102                 Alvarado
#         CS103                 Rich
#         NT110                 Burke
#         CM241                 Lee

# The program should also create a dictionary containing course numbers and the meeting times of each course.
#   The dictionary should have the following key-value pairs:

#     |Course Number(key)|    |Meeting Time(value)|
#         CS101                 8:00 a.m.
#         CS102                 9:00 a.m.
#         CS103                 10:00 a.m.
#         NT110                 11:00 a.m.
#         CM241                 1:00 p.m.

# The program should let the user enter a course number, then it should display the course's room number, instructor,
#   and meeting times.



def course_info():

  courses = ['CS101', 'CS102', 'CS103', 'NT110', 'CM241']

  courses_info = {
    'CS101': [3004, 'Haynes', '8:00 a.m.'],
    'CS102': [4501, 'Alvarado', '9:00 a.m.'],
    'CS103': [6755, 'Rich', '10:00 a.m.'],
    'NT110': [1244, 'Burke', '11:00 a.m.'],
    'CM241': [1411, 'Lee', '1:00 p.m.']
  }  

  def user_selection():
    print(courses)
    user_input = input('What course would you like to take?: ').upper()


    if user_input in courses_info:
      if user_input == 'CS101':
        print('*' * 40)
        print(f'You have chosen {user_input}')
        print(f'Room number: {courses_info["CS101"][0]}')
        print(f'With instructor: {courses_info["CS101"][1]}')
        print(f'At {courses_info["CS101"][2]}')
        print('*' * 40)
      elif user_input == 'CS102':
        print('*' * 40)
        print(f'You have chosen {user_input}')
        print(f'Room number: {courses_info["CS102"][0]}')
        print(f'With instructor: {courses_info["CS102"][1]}')
        print(f'At {courses_info["CS102"][2]}')
        print('*' * 40)
      elif user_input == 'CS103':
        print('*' * 40)
        print(f'You have chosen {user_input}')
        print(f'Room number: {courses_info["CS103"][0]}')
        print(f'With instructor: {courses_info["CS103"][1]}')
        print(f'At {courses_info["CS103"][2]}')
        print('*' * 40)
      elif user_input == 'NT110':
        print('*' * 40)
        print(f'You have chosen {user_input}')
        print(f'Room number: {courses_info["NT110"][0]}')
        print(f'With instructor: {courses_info["NT110"][1]}')
        print(f'At {courses_info["NT110"][2]}')
        print('*' * 40)
      elif user_input == 'CM241':
        print('*' * 40)
        print(f'You have chosen {user_input}')
        print(f'Room number: {courses_info["CM241"][0]}')
        print(f'With instructor: {courses_info["CM241"][1]}')
        print(f'At {courses_info["CM241"][2]}')
        print('*' * 40)
    else:
      print(f'{user_input} is an invalid class number')
      user_selection()

  user_selection()

course_info()
