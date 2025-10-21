import pygame
import time

pygame.init()

my_sound = pygame.mixer.Sound(
    "/Users/randy/development/p1-36-Smart-Proximity-Alarm-2025-v1/sound samples/drum_cymbal_hard.wav"
)

# my_sound.play()

time.sleep(3)

drum = pygame.mixer.Sound(
    "/Users/randy/development/p1-36-Smart-Proximity-Alarm-2025-v1/sound samples/drum_bass_hard.wav"
)
bell = pygame.mixer.Sound(
    "/Users/randy/development/p1-36-Smart-Proximity-Alarm-2025-v1/sound samples/perc_bell.wav"
)
bird = pygame.mixer.Sound(
    "/Users/randy/development/p1-36-Smart-Proximity-Alarm-2025-v1/sound samples/misc_crow.wav"
)
guitar = pygame.mixer.Sound(
    "/Users/randy/development/p1-36-Smart-Proximity-Alarm-2025-v1/sound samples/guit_harmonics.wav"
)

# drum.play()
# bell.play()
# bird.play()
# guitar.play()

time.sleep(3)

from gpiozero import Button, LED

btn = Button(17)
led = LED(4)
btn.when_pressed = led.on
btn.when_released = led.off
