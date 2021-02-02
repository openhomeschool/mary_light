# Import the libraries we'll need:
import socket # more (very detailed) information at https://docs.python.org/3/library/select.html
import select # more (very detailed) information at https://docs.python.org/3/library/socket.html
import sys # more (very detailed) information at https://docs.python.org/3/library/sys.html
from thread import start_new_thread

import main

# Constants:
ADDRESS = ('0.0.0.0', 8002)

# Functions:
def create_server():
	# Make calls to libraries to do magical mysterious things to make the kind of server we want:
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	server.bind(ADDRESS) 
	server.listen(100) # tells the server to listen for up to 100 simultaneous connections; this could have been specified as a CONSTANT at the top of the file, after ADDRESS
	# (learn more about these magical arguments at https://docs.python.org/3/library/socket.html)
	# Now that our server is all set up, we "return" it to the caller of this function:
	return server


def client_thread(connection, address): 
	# Send a "welcome" message to the client who just connected to us, which started this thread:
	connection.send("Welcome to the 'Mary server'!  Type 'b' (then Enter) to begin, 'f' (then Enter) for 'faster' playback, or 's' (then Enter) for 'slower' playback.")

	# Loop until this connection dies: 
	while True: # 'break', below, will finally break us out of this (otherwise 'forever') loop
		try:
			# Receive ('recv') as many as 2,048 characters that were sent.  Why 2048?  That's another study.  You could certainly change this number.
			message = connection.recv(2048) 
			if message: # i.e., if there was actually any text in the message sent...
				message = message.decode("utf-8")
				print(message)
				for character in str(message):
					if character == 'b':
						main.begin()
					elif character == 's':
						main.slower()
					elif character == 'f':
						main.faster()

			else:
				# The incoming message had no text at all. This tends to mean that the connection is broken, so we break out of our while loop:
				break

		except:
			# Any other trouble we have, we'll assume is not important enough to treat now, but an improvement would be to at least print something to the screen to indicate that there was trouble
			continue # this is like "pass", above, but it specifically means to start over at the top of the "while" loop.
			# In this case, since there is no code in this function below, "continue" would do the same thing as "pass"


# And here begins the actual main program, as everything above was just code that defined constants,
# global variables, and functions.  If the rest of this file was empty, this "program" would do
# nothing at all.  The code below is not inside of a function, so it will get executed when the
# program is run, but, when the code below needs to use the constants or functions defined above,
# then it can call them by name.  When the function, above, is called by name, it will finally be
# run, or "executed", as it's often called in software development.

server = create_server() # Actually create the server

main.init() # Initialize the LEDs

# This "while True:" is just a never-ending loop.  The code below, within, will run, top to bottom,
# over and over again until you forcibly kill it (e.g., by pressing Control-C while it's running
# in your terminal).
while True: 
	
	# Accept connections that clients are asking us to accept (this is like picking up the phone when it's ringing):
	connection, address = server.accept() 

	# Print the IP address of the client that just connected, just to inform anybody watching the server directly:
	print(address[0] + " connected")

	# Start the thread that will process this connection's messages until it is finally closed (by the user, or by the server shut-down):
	start_new_thread(client_thread, (connection, address))

server.close() 

