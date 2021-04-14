#!/usr/bin/env python3

import coverpy, subprocess, sys, os, requests, time
coverpy = coverpy.CoverPy()
# Set a limit. There is a default (1), but I set it manually to showcase usage.
limit = 1

def do_it():
    try:
        songname = subprocess.getoutput("playerctl metadata --format '{{artist}} {{title}} {{album}}'")
        result = coverpy.get_cover(songname, limit)
        url = result.artwork(300)
        r = requests.get(url)
        open('/home/williammagland/.tmp/albumart', 'wb').write(r.content)
        time.sleep(1)
    except Exception:
        pass
while True:
    do_it()
# try:
# 	result = coverpy.get_cover("OK Computer", limit)
# 	# Set a size for the artwork (first parameter) and get the result url.
# 	print(result.name)
# 	print(result.artwork(100))
# except coverpy.exceptions.NoResultsException:
# 	print("Nothing found.")
# except requests.exceptions.HTTPError:
# 	print("Could not execute GET request")

# import requests

# def download_image(url)
# url = 'http://google.com/favicon.ico'
# filename = url.split('/')[-1]
# r = requests.get(url, allow_redirects=True)
# open(filename, 'wb').write(r.content)
