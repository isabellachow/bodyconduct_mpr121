#!/usr/bin/env python

"""beetbox.py: Trigger script for the BeetBox."""

__author__ = "Scott Garner"
__email__ = "scott@j38.net"

import pygame

import RPi.GPIO as GPIO
import mpr121

# Use GPIO Interrupt Pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else

mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5a)

# User pygame for sounds

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

soundone = pygame.mixer.Sound('samples/soundone.wav')
soundone.set_volume(.65);
soundtwo = pygame.mixer.Sound('samples/soundtwo.wav')
soundtwo.set_volume(.65);
soundone = pygame.mixer.Sound('samples/soundone.wav')
soundone.set_volume(.65);
soundtwo = pygame.mixer.Sound('samples/soundtwo.wav')
soundtwo.set_volume(.65);
soundone = pygame.mixer.Sound('samples/soundone.wav')
soundone.set_volume(.65);
soundtwo = pygame.mixer.Sound('samples/soundtwo.wav')
soundtwo.set_volume(.65);

# Track touches

touches = [0,0,0,0,0,0];

while True:

	if (GPIO.input(7)): # Interupt pin is high
		pass
	else: # Interupt pin is low

		touchData = mpr121.readData(0x5a)

		for i in range(6):
			if (touchData & (1<<i)):

				if (touches[i] == 0):

					print( 'Pin ' + str(i) + ' was just touched')

					if (i == 0):
						soundone.play()
					elif (i == 1):
						soundtwo.play()
					elif (i == 2):
						soundone.play()
					elif (i == 3):
						soundtwo.play()
					elif (i == 4):
						soundone.play()
					elif (i == 5):
						soundtwo.play()

				touches[i] = 1;
			else:
				if (touches[i] == 1):
					print( 'Pin ' + str(i) + ' was just released')
				touches[i] = 0;
