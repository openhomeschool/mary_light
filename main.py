from gpiozero import LED
from time import sleep

leds = [ LED(2), LED(3), LED(4) ]

# Turn everything off
for led in leds:
	led.off()

DURATION_MULTIPLIER = 0.2
REST = 0.1

# Light
def light(led_number, duration):
	led_index = led_number - 1
	leds[led_index].on()
	sleep(duration * DURATION_MULTIPLIER)
	leds[led_index].off()
	sleep(REST)

# Mary Had A Little Lamb:
notes = [ 
		# Each tuple is (led_number, duration); a duration of 1 is a quarter note; 2 = half note, 4 = whole note
		(3, 1), (2, 1), (1, 1), (2, 1), (3, 1), (3, 1), (3, 2),
		(2, 1), (2, 1), (2, 2),
		(3, 1), (3, 1), (3, 2),

		(3, 1), (2, 1), (1, 1), (2, 1), (3, 1), (3, 1), (3, 1),
		(3, 1), (2, 1), (2, 1), (3, 1), (2, 1), (1, 4),
	]

for led, duration in notes:
	light(led, duration)

sleep(1) # take a bow

