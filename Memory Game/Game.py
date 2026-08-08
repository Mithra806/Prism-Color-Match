from gpiozero import RGBLED, Button
from time import sleep
from random import choice


#LEDs
led = RGBLED( red=5, green = 17, blue=27)

gbutton = Button(18)

bbutton = Button(23)

rbutton = Button(16)

colors = {
    "red": (1, 0, 0),
    "green": (0, 1, 0),
    "blue": (0, 0, 1),
}

def flash_color(name, duration = 0.6, gap = 0.2):
    led.color = colors[name]
    sleep(duration)
    led.off()
    sleep(gap)

def flash_sequence(sequence):
    for name in sequence:
        flash_color(name)

def flash_success():
    quick = ["green", "blue", "red", "red", "blue", "green"]
    for name in quick:
        flash_color(name, duration = 0.15, gap = 0.1)

def flash_fail():
    for _ in range(3):
        flash_color("red", duration = 0.3, gap = 0.15)

def get_user_input(length):
    guess = []
    for _ in range(length):
        pressed = wait_for_any_button()
        flash_color(pressed, duration = 0.3, gap = 0.05)
        guess.append(pressed)
    return guess

def wait_for_any_button():
    while True:
        if gbutton.is_pressed:
            wait_release(gbutton)
            return "green"
        if bbutton.is_pressed:
            wait_release(bbutton)
            return "blue"
        if rbutton.is_pressed:
            wait_release(rbutton)
            return "red"
        sleep(0.01)

def wait_release(button):
    while button.is_pressed:
        sleep(0.01)

try:
    level = 3
    sequence = []

    while True:
        while len(sequence) < level:
            sequence.append(choice(list(colors.keys())))

        print(f"Level {level} : {sequence}")
        sleep(1)
        flash_sequence(sequence)

        guess = get_user_input(level)

        if guess == sequence:
            print("Correct!")
            flash_success()
            level += 1

        else:
            print("Wrong!")
            flash_fail()
            level=3
            sequence = []

        sleep(0.5)

finally:
    led.off()