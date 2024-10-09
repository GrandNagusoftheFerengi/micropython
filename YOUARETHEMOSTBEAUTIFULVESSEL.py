import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)

# Morse code timing (in seconds)
DOT_DURATION = 0.2
DASH_DURATION = 0.6
ELEMENT_GAP = 0.2
LETTER_GAP = 0.6
WORD_GAP = 1.4

def dot():
    led.value(1)
    utime.sleep(DOT_DURATION)
    led.valueimport machine
import utime

led = machine.Pin(15, machine.Pin.OUT)

# Morse code timing (in seconds)
DOT_DURATION = 0.2
DASH_DURATION = 0.6
ELEMENT_GAP = 0.2
LETTER_GAP = 0.6
WORD_GAP = 1.4

def dot():
    led.value(1)
    utime.sleep(DOT_DURATION)
    led.value(0)
    utime.sleep(ELEMENT_GAP)

def dash():
    led.value(1)
    utime.sleep(DASH_DURATION)
    led.value(0)
    utime.sleep(ELEMENT_GAP)

def letter_gap():
    utime.sleep(LETTER_GAP - ELEMENT_GAP)  # Subtract ELEMENT_GAP because it's already added after each element

def word_gap():
    utime.sleep(WORD_GAP - ELEMENT_GAP)  # Subtract ELEMENT_GAP because it's already added after each element

def blink_morse_char(char):
    if char == '.':
        dot()
    elif char == '-':
        dash()
    elif char == ' ':
        word_gap()
    else:
        letter_gap()

def blink_message(message):
    for char in message:
        blink_morse_char(char)
    word_gap()  # Add a word gap at the end of the message

morse_message = "-.-- --- ..- / .- .-. . / - .... . / -- --- ... - / -... . .- ..- - .. ..-. ..- .-.. / ...- . ... ... . .-.. / .. -. / - .... . / .-- --- .-. .-.. -.."

while True:
    blink_message(morse_message)(0)
    utime.sleep(ELEMENT_GAP)

def dash():
    led.value(1)
    utime.sleep(DASH_DURATION)
    led.value(0)
    utime.sleep(ELEMENT_GAP)

def letter_gap():
    utime.sleep(LETTER_GAP - ELEMENT_GAP)  # Subtract ELEMENT_GAP because it's already added after each element

def word_gap():
    utime.sleep(WORD_GAP - ELEMENT_GAP)  # Subtract ELEMENT_GAP because it's already added after each element
