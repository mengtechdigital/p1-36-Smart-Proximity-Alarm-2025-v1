import pygame
import time

pygame.init()

my_sound = pygame.mixer.Sound(
    "/Users/randy/development/p1-36-Smart-Proximity-Alarm-2025-v1/sound samples/drum_cymbal_hard.wav"
)

my_sound.play()

time.sleep(3)
