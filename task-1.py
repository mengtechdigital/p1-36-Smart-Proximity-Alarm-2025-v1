from gpiozero import Button, LED
import time
import pygame

pygame.init()


drum = pygame.mixer.Sound(
    "/home/pi/work/gpio-music-box/sound samples/drum_bass_hard.wav"
)
bell = pygame.mixer.Sound("/home/pi/work/gpio-music-box/sound samples/perc_bell.wav")
bird = pygame.mixer.Sound("/home/pi/work/gpio-music-box/sound samples/misc_crow.wav")
guitar = pygame.mixer.Sound(
    "/home/pi/work/gpio-music-box/sound samples/guit_harmonics.wav"
)

btn_bell = Button(17)


btn_bell.when_pressed = bell.play
time.sleep(100)
