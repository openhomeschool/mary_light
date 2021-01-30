from gpiozero import LED
from time import sleep

leds = [ LED(2), LED(3), LED(4) ]

# Turn everything off
for led in leds:
	led.off()

DURATION_MULTIPLIER = 0.2
REST = 0.1

# Light
def light(led, duration):
	led.on()
	sleep(duration * DURATION_MULTIPLIER)
	led.off()
	sleep(RESAT)

# Mary Had A Little Lamb:
notes = [ # value, duration
					(3, 1),
					(2, 1),
					(1, 1),
					(2, 1),
					(3, 1),
					(3, 1),
					(3, 2),
					(2, 1),
					(2, 1),
					(2, 2),
					(3, 1),
					(3, 1),
					(3, 2),
					(3, 1),

					(3, 1),
					(2, 1),
					(1, 1),
					(2, 1),
					(3, 1),
					(3, 1),
					(3, 1),
					(3, 1),
					(2, 1),
					(2, 1),
					(3, 1),
					(2, 1),
					(1, 4),
	]

for led, duration in notes:
	light(led, duration)
