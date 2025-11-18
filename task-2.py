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


led1 = LED(4)
led2 = LED(5)
led3 = LED(6)
led4 = LED(7)

btn_drum = Button(17)
btn_bell = Button(22)
btn_bird = Button(23)
btn_guitar = Button(27)

while True:
    btn_drum.when_pressed = drum.play
    time.sleep(0.1)
    btn_drum.when_pressed = led1.on
    btn_drum.when_released = led1.off
    btn_bell.when_pressed = bell.play
    time.sleep(0.1)
    btn_bell.when_pressed = led2.on
    btn_bell.when_released = led2.off
    btn_bird.when_pressed = bird.play
    time.sleep(0.1)
    btn_bird.when_pressed = led3.on
    btn_bird.when_released = led3.off
    btn_guitar.when_pressed = guitar.play
    time.sleep(0.1)
    btn_guitar.when_pressed = led4.on
    btn_guitar.when_released = led4.off
