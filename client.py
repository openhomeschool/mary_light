# Import the libraries we'll need:
import socket  
import select
import sys

# Constants:
ADDRESS = ('localhost', 8002)

# Code:

# Create the socket and connect it to the server:
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # this appears to be a magical, mysterious line of code; you can learn more at https://docs.python.org/3/library/socket.html
connection.connect(ADDRESS) 

# We will "try" to send and recieve all the messages we can, but if there's an error, our program
# will kick down to the "except:" bracket, at the bottom...
try:
	
	# We will simply run this same bit of code, top to bottom, over and over and over, until the
	# connection is closed on us or you press "Control-C" to quit.
	while True: 

		# Look for any input, either from the 'connection' or from the user's own keyboard (sys.stdin):
		readers, writers, errors = select.select((connection, sys.stdin), (), ())

		for reader in readers:
			if reader == connection:
				# A message from the server!  Receive it, and print it:
				# (note that the server doesn't currently send any messages; this is just set up for future possibilities, such as "play", "end" feedback)
				message = reader.recv(2048) # Why 2048?  That's another study.  You could certainly change this number, with thoughtfulness.
				if message:
					print(message) # this makes the message print out onto your screen
				else:
					# There was nothing in the message, which usually means that the connection closed
					raise # this "raises an exception", causing the program to jump down to the "except" clause and finish, as there's nothing more to do
			else:
				# If the reader was not the connection to the server, then the "input" we have to read 
				# is a message that the user running this 'client.py' program actually typed in, and so
				# we need to read that, and then send it to the server over our 'connection':
				message = sys.stdin.readline() # the message became available when the user pressed "Enter", and so it's one "line" of text
				connection.send(message) 
				# Notice that we do nothing here to "check" the user's input as "valid" - the server will simply ignore any invalid commands.
				# A user should really only be typing a 'b' (for begin), 'f' (for faster), or 's' (for slower), or any combination of these.

except:
	# Either something went wrong, or, more likely, our program was intentionally interrupted,
	# meaning that the user running this (client.py) program, himself (or herself), pressed Control-C
	# in order to stop the program, or the server closed the connection, so we no longer have a way
	# to send or receive messages anyway.  For now, all we'll do is try to close our connection to
	# the server (if it isn't already closed), and let our program end.
	connection.close()
