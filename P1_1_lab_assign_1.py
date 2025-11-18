import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
BUZZER = 26

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)


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


def beep_freq(d):
    print(d, "cm")
    if d > 50:
        return -1
    elif 50 >= d >= 30:
        return 1
    elif 30 > d >= 20:
        return 0.5
    elif 20 > d >= 10:
        return 0.25
    else:  # d < 10
        return 0


try:
    while True:
        distance = distance_cm()
        detected_beep_frequency = beep_freq(distance)

        if detected_beep_frequency == -1:
            GPIO.output(BUZZER, GPIO.LOW)
            time.sleep(0.25)
        elif detected_beep_frequency == 0:
            GPIO.output(BUZZER, GPIO.HIGH)
            time.sleep(0.25)
        else:
            GPIO.output(BUZZER, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(BUZZER, GPIO.LOW)
            time.sleep(detected_beep_frequency)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
