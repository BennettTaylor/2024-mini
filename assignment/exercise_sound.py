#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def playnote(note) -> None:
    if note == "C":
        quiet()
        utime.sleep(0.25)
        freq = 262
        playtone(freq, 0.25)
    elif note == "D":
        quiet()
        utime.sleep(0.25)
        freq = 294
        playtone(freq, 0.25)
    elif note == "E":
        quiet()
        utime.sleep(0.25)
        freq = 330
        playtone(freq, 0.25)
    elif note == "F":
        quiet()
        utime.sleep(0.25)
        freq = 349
        playtone(freq, 0.25)
    elif note == "G":
        quiet()
        utime.sleep(0.25)
        freq = 392
        playtone(freq, 0.25)
    elif note == "A":
        quiet()
        utime.sleep(0.25)
        freq = 440
        playtone(freq, 0.25)
    elif note == "B":
        quiet()
        utime.sleep(0.25)
        freq = 494
        playtone(freq, 0.25)


def quiet():
    speaker.duty_u16(0)


freq: float = 30
duration: float = 0.1  # seconds

print("Playing frequency (Hz):")

playnote("C")
playnote("C")
playnote("G")
playnote("G")
playnote("A")
playnote("A")
playnote("F")
playnote("F")
playnote("E")
playnote("E")
playnote("D")
playnote("D")
playnote("C")
playnote("G")
playnote("G")
playnote("F")
playnote("F")
playnote("E")
playnote("E")
playnote("D")
playnote("G")
playnote("G")
playnote("F")
playnote("F")
playnote("E")
playnote("E")



# Turn off the PWM
quiet()
