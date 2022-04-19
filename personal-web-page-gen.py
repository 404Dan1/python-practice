# PERSONAL WEB PAGE GENERATOR

# Write a program that asks the user for his or her name, then ask the user to enter a sentence that describes
#   himself or herself.

# Once the user has entered the requested input, the program should create an HTML file, containing the input,
#   for a simple Web page. Here is an example of the HTML content

'''
<html>
<head>
</head>
<body>
    <center>
        <h1>Your Name</h1>
    </center>
    <hr />
      Your Bio
    <hr />
</body>
</html>
'''

def your_name():
  person_name = input("What is your name?: ")
  return person_name


def your_bio():
  person_bio = input("What is your background?: ")
  return person_bio


def your_web(person_name, person_bio):
  person_web = "King.html"
  open_file = open(person_web, "w+")


  open_file.write(
    f"<html>\n<head>\n</head>\n<body>\n\t<center>\n\t\t<h1>{person_name}</h1>\n\t</center>\n\t<hr />\n\t{person_bio}\n\t<hr />\n</body>\n</html>"
  )


  open_file.close()


your_web(your_name(), your_bio())

