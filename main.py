from gpiozero import LED
from time import sleep

led1 = LED(2)
led2 = LED(3)
led3 = LED(4)

# Turn everything off
led1.off()
led2.off()
led3.off()

# Light
def light(led, duration):
	led.on()
	sleep(duration)
	led.off()
	sleep(0.1)

	
# Mary Had A Little Lamb:
light(led3, 0.2)
light(led2, 0.2)
light(led1, 0.2)
light(led2, 0.2)
light(led3, 0.2)
light(led3, 0.2)
light(led3, 0.4)
light(led2, 0.2)
light(led2, 0.2)
light(led2, 0.4)
light(led3, 0.2)
light(led3, 0.2)
light(led3, 0.4)

light(led3, 0.2)
light(led2, 0.2)
light(led1, 0.2)
light(led2, 0.2)
light(led3, 0.2)
light(led3, 0.2)
light(led3, 0.2)
light(led3, 0.2)
light(led2, 0.2)
light(led2, 0.2)
light(led3, 0.2)
light(led2, 0.2)
light(led1, 0.8)

