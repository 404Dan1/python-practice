
import telnetlib
import time

# example Telnet
host = '10.0.0.1'  # IP address of the router
port = '23'  # the port number for Telnet server
user = 'admin'  # the user of the telnet server

password = 'admin'

# set up the telnet client with the variables we've created
tel = telnetlib.Telnet(host=host, port=port)

tel.read_until(b'Username: ')  # tells the script to pause, allows the user to enter the username
tel.write(user.encode() + b'\n')

tel.read_until(b'Password: ')  # same with the username, allows the user to enter the password
tel.write(password.encode() + b'\n')

tel.write(b'terminal length 0\n')
tel.write(b'show ip interface brief\n')  # this sends a command to the telnet
tel.write(b'exit\n')
time.sleep(2)

output = tel.read_all()  # reads all the output of the command in the terminal


output = output.decode()

print(output)
