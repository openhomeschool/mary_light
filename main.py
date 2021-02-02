# Import the libraries we'll need:
from gpiozero import LED
from time import sleep
import musicalbeeps

# Constants:
DURATION_MULTIPLIER_INCREMENT = 0.02
MIN_DURATION_MULTIPLIER = 0.10
MAX_DURATION_MULTIPLIER = 0.50
PITCH_LIGHT_DELAY = 0.2

# Variables:
leds = [ LED(2), LED(3), LED(4) ]
pitches = ['C', 'D', 'E'] # must be the same size as `leds`, above
duration_multiplier = 0.2
rest = 0.1

# Code:

player = musicalbeeps.Player(volume = 1.0)

# Turn everything off
def init():
	for led in leds:
		led.off()

# Light
def light(led_number, duration):
	# Turn the LED on:
	led_index = led_number - 1
	player.play_note(pitches[led_index], duration * duration_multiplier)
	sleep(PITCH_LIGHT_DELAY)
	leds[led_index].on()
	# Leave it on for the right amount of time:
	sleep(duration * duration_multiplier)
	
	# Then turn it off (for a rest period):
	leds[led_index].off()
	sleep(rest * duration_multiplier)

# Mary Had A Little Lamb:
notes = [ 
		# Each tuple is (led_number, duration); a duration of 1 is a quarter note; 2 = half note, 4 = whole note
		(3, 1), (2, 1), (1, 1), (2, 1), (3, 1), (3, 1), (3, 2),
		(2, 1), (2, 1), (2, 2),
		(3, 1), (3, 1), (3, 2),

		(3, 1), (2, 1), (1, 1), (2, 1), (3, 1), (3, 1), (3, 1),
		(3, 1), (2, 1), (2, 1), (3, 1), (2, 1), (1, 4),
	]

running = False
def begin():
	global running
	if not running:
		running = True
		for led, duration in notes:
			light(led, duration)
		sleep(1) # take a bow
	running = False

def faster():
	global duration_multiplier
	duration_multiplier -= DURATION_MULTIPLIER_INCREMENT
	if duration_multiplier < MIN_DURATION_MULTIPLIER:
		duration_multiplier = MIN_DURATION_MULTIPLIER
	print("decreased duration_multiplier to: %1.2f" % duration_multiplier)

def slower():
	global duration_multiplier
	duration_multiplier += DURATION_MULTIPLIER_INCREMENT
	if duration_multiplier > MAX_DURATION_MULTIPLIER:
		duration_multiplier = MAX_DURATION_MULTIPLIER
	print("increased duration_multiplier to: %1.2f" % duration_multiplier)

