import pygame
import time
import RPi.GPIO as GPIO

pygame.init()

# Update <fileN>.wav to actual filenames
a1 = pygame.mixer.Sound("/home/pi/gpio_music_box/lab/<file1>.wav")  # 50–30 cm
a2 = pygame.mixer.Sound("/home/pi/gpio_music_box/lab/<file2>.wav")  # 30–20 cm
a3 = pygame.mixer.Sound("/home/pi/gpio_music_box/lab/<file3>.wav")  # 20–10 cm
a4 = pygame.mixer.Sound("/home/pi/gpio_music_box/lab/<file4>.wav")  # < 10 cm

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def distance_cm():
    GPIO.output(TRIG, False)
    time.sleep(0.1)

    GPIO.output(TRIG, True)
    time.sleep(0.1)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        end = time.time()

    pulse = end - start
    dist = pulse * 17150.0  # (34300 cm/s) / 2
    return round(dist, 1)


def band_for_distance(d):
    if d > 50:
        return 0
    elif 50 >= d >= 30:
        return 1
    elif 30 > d >= 20:
        return 2
    elif 20 > d >= 10:
        return 3
    else:  # d < 10
        return 4


sounds = {1: a1, 2: a2, 3: a3, 4: a4}

try:
    prev_band = None
    while True:
        d = distance_cm()
        band = band_for_distance(d)

        if band != prev_band:
            if band in sounds:
                sounds[band].play()
            prev_band = band

        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    pygame.quit()
