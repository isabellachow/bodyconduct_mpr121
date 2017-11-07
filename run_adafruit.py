# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
import time
import pygame

import Adafruit_MPR121.MPR121 as MPR121

# Thanks to Scott Garner & BeetBox!
# https://github.com/scottgarner/BeetBox/

print 'Adafruit MPR121 Capacitive Touch Audio Player Test'

# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device, and
# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

# Alternatively, specify a custom I2C address such as 0x5B (ADDR tied to 3.3V),
# 0x5C (ADDR tied to SDA), or 0x5D (ADDR tied to SCL).
#cap.begin(address=0x5B)

# Also you can specify an optional I2C bus with the bus keyword parameter.
#cap.begin(busnum=1)

pygame.mixer.pre_init(48000, -16, 1, 1024)
pygame.init()

# Define mapping of capacitive touch pin presses to sound files
# tons more sounds are available but because they have changed to .flac in /opt/sonic-pi/etc/samples/ some will not work
# more .wav files are found in /usr/share/scratch/Media/Sounds/ that work fine this example uses Aniamal sounds.

sound1 = pygame.mixer.Sound("/home/pi/bodyconduct_mpr121/samples/soundone.wav")
soundChannel1 = pygame.mixer.Channel(1)
soundList[0] = sound1
soundChannelList[0] = soundChannel1
sound2 = pygame.mixer.Sound("/home/pi//bodyconduct_mpr121/samples/soundtwo.wav")
soundChannel2 = pygame.mixer.Channel(2)
soundList[1] = sound2
soundChannelList[1] = soundChannel2
sound3 = pygame.mixer.Sound("/home/pi/bodyconduct_mpr121/samples/soundone.wav")
soundChannel3 = pygame.mixer.Channel(3)
soundList[2] = sound3
soundChannelList[2] = soundChannel3
sound4 = pygame.mixer.Sound("/home/pi//bodyconduct_mpr121/samples/soundtwo.wav")
soundChannel4 = pygame.mixer.Channel(4)
soundList[3] = sound4
soundChannelList[3] = soundChannel4
sound5 = pygame.mixer.Sound("/home/pi/bodyconduct_mpr121/samples/soundone.wav")
soundChannel5 = pygame.mixer.Channel(5)
soundList[4] = sound5
soundChannelList[4] = soundChannel5
sound6 = pygame.mixer.Sound("/home/pi//bodyconduct_mpr121/samples/soundtwo.wav")
soundChannel6 = pygame.mixer.Channel(6)
soundList[5] = sound6
soundChannelList[5] = soundChannel6
sound7 = pygame.mixer.Sound("/home/pi/bodyconduct_mpr121/samples/soundone.wav")
soundChannel7 = pygame.mixer.Channel(7)
soundList[6] = sound7
soundChannelList[6] = soundChannel7
sound8 = pygame.mixer.Sound("/home/pi//bodyconduct_mpr121/samples/soundtwo.wav")
soundChannel8 = pygame.mixer.Channel(1)
soundList[7] = sound8
soundChannelList[7] = soundChannel8
sound9 = pygame.mixer.Sound("/home/pi/bodyconduct_mpr121/samples/soundone.wav")
soundChannel9 = pygame.mixer.Channel(2)
soundList[8] = sound9
soundChannelList[8] = soundChannel9
sound10 = pygame.mixer.Sound("/home/pi//bodyconduct_mpr121/samples/soundtwo.wav")
soundChannel10 = pygame.mixer.Channel(3)
soundList[9] = sound10
soundChannelList[9] = soundChannel10
sound11 = pygame.mixer.Sound("/home/pi/bodyconduct_mpr121/samples/soundone.wav")
soundChannel11 = pygame.mixer.Channel(4)
soundList[10] = sound11
soundChannelList[10] = soundChannel11
sound12 = pygame.mixer.Sound("/home/pi//bodyconduct_mpr121/samples/soundtwo.wav")
soundChannel12 = pygame.mixer.Channel(5)
soundList[11] = sound12
soundChannelList[11] = soundChannel12
print "Soundboard Ready."

# Main loop to print a message every time a pin is touched.
print('Press Ctrl-C to quit.')
last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    # Check each pin's last and current state to see if it was pressed or released.
    for i in range(12):
        # Each pin is represented by a bit in the touched value.  A value of 1
        # means the pin is being touched, and 0 means it is not being touched.
        pin_bit = 1 << i
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            print('{0} touched!'.format(i))
            if (sounds[i]):
                sounds[i].play()
        if not current_touched & pin_bit and last_touched & pin_bit:
            print('{0} released!'.format(i))

    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    time.sleep(0.1)

    # Alternatively, if you only care about checking one or a few pins you can
    # call the is_touched method with a pin number to directly check that pin.
    # This will be a little slower than the above code for checking a lot of pins.
    #if cap.is_touched(0):
    #    print('Pin 0 is being touched!')

    # If you're curious or want to see debug info for each pin, uncomment the
    # following lines:
    #print('\t\t\t\t\t\t\t\t\t\t\t\t\t 0x{0:0X}'.format(cap.touched()))
    #filtered = [cap.filtered_data(i) for i in range(12)]
    #print('Filt:', '\t'.join(map(str, filtered)))
    #base = [cap.baseline_data(i) for i in range(12)]
    #print('Base:', '\t'.join(map(str, base)))
