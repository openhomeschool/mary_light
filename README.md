# The "mary_light" project
## openhome.school Computer Class

This project will combine the skills you explored in the first two weeks: "light", for turning on
an LED via GPIO pins, and "hello_friends", for transmitting information over a network via sockets.

## The Prototype Idea

The idea behind this "prototype" is to blink lights according to the melody sequence "Mary Had a
Little Lamb" - one (color) LED for each note - while playing those notes through a bluetooth
speaker.

**A prototype is an explorationa or demonstration project that might be developed into a real
product. **

The "real product" would be a stuffed animal (or other toy) with LEDs which "play" to a song in
the proper musical sequence, **while** the song is playing through a bluetooth speaker.  To make it
as cool as possible, and make use of sockets, the prototype will be a server, controlled by one or
more client computers.  After initial testing on a class Raspberry Pi 400, the prototype will be
deployed on a Pi Zero - a very small version of the Raspberry Pi, and powered by battery, and tucked
inside of a prototype stuffed animal.

## The Details

Many details will be skipped in this README; it is expected that the course instructor will guide
the prototype development.  Among the gotchas are these:

* Getting an appropriate Pi Zero "ISO" image onto an SD card via dd or other mechanism
* Logging into the booted Pi Zero via SSH (or hooking it to an HDMI monitor and wireless keyboard)
* Setting up bluez bluetooth on the Pi Zero, and pairing and connecting to a bluetooth speaker via bluetoothctl
* Wiring to the Pi Zero GPIO pins, which may involve soldering or trickery

All of this, and more, is treated in the tutor companion guide.

...
