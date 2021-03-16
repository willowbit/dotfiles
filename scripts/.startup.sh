#!/bin/bash

xrandr --output HDMI1 --auto --left-of eDP1 --primary
wallpapername="Shore.jpg"
feh --bg-fill ~/wallpapers/$wallpapername
guake
picom
killall spotifyd
spotifyd --config-path ~/.config/spotifyd/config --no-daemon
