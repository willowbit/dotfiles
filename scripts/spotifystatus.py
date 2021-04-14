#!/usr/bin/env python
import subprocess, sys

device = subprocess.getoutput("spotify devices").splitlines()
volume = subprocess.getoutput("playerctl volume").split('.')[0]
song = subprocess.getoutput("playerctl metadata --format '{{artist}} - {{title}}'")

for thing in device:
    if thing.split()[0] == '*':
        device = thing.split()[1]

try:
    if sys.argv[1] == '-s':
        if 'player' in song.split():
            print()
            pass
        else:
            print(song)
    if sys.argv[1] == '-v':
        print(volume)
except Exception as e:
    pass
