#!/usr/bin/env python
import subprocess, sys
try:
    song = subprocess.getoutput("spotify status").split('Playing:')[1].splitlines()[0].strip()
    artist = subprocess.getoutput("spotify status").splitlines()[1].strip().split('-')[0]
    device = subprocess.getoutput("spotify devices").splitlines()
    devicelist = subprocess.getoutput("spotify devices").splitlines()
    volume = subprocess.getoutput("spotify volume up 0")
    for thing in device:
        if thing.split()[0] == '*':
            device = thing.split()[1]
    for thing in devicelist:
        if thing.split()[0] == '*':
            devicelist.remove(thing)
            devicelist.append(thing.split()[1])
except Exception:
    pass

try:
    def switch_device():
        devicelist.remove(device)
        # print(devicelist)
        target = devicelist[0].strip()
        print(target)
        subprocess.getoutput(f"spotify devices -s {target}")
    if sys.argv[1] == '-s':
        if len(list(song)) > 28:
            song = ''.join(list(song)[0:28])
            print(f'{song}... ')
        else:
            print(f'{song} -')
            song = None
    if sys.argv[1] == '-a':
        print(f'{artist}')
    if sys.argv[1] == '-d':
        print(device)
    if sys.argv[1] == '-v':
        print(volume.split()[3])
    if sys.argv[1] == '--switch-device':
            switch_device()
except Exception:
    print('no music')
    pass