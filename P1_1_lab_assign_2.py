import pygame
import time
import RPi.GPIO as GPIO

pygame.init()
pygame.mixer.set_num_channels(1)

a1 = pygame.mixer.Sound("/home/pi/work/gpio-music-box/50cm.wav")  # 50–30 cm
a2 = pygame.mixer.Sound("/home/pi/work/gpio-music-box/30cm.wav")  # 30–20 cm
a3 = pygame.mixer.Sound("/home/pi/work/gpio-music-box/20cm.wav")  # 20–10 cm
a4 = pygame.mixer.Sound("/home/pi/work/gpio-music-box/10cm.wav")  # < 10 cm

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def distance_cm():
    print("Distance Measurement in Progress")
    GPIO.output(TRIG, False)
    time.sleep(0.1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        end = time.time()

    pulse = end - start
    dist = pulse * 17150  # (34300 cm/s) / 2
    return round(dist, 1)


def band_for_distance(d):
    print(d, "cm")
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
    current_playing_band = None
    playing = False
    while True:
        distance = distance_cm()
        band = band_for_distance(distance)

        if band in sounds:
            if not playing or band > (current_playing_band or 0):
                current_playing_band = band
                playing = True
                sounds[band].play()
        prev_band = band

        if playing and not pygame.mixer.Channel(0).get_busy():
            playing = False
            current_playing_band = None

        time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    pygame.quit()
