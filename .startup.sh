#!/bin/bash

xrandr --output HDMI1 --auto --left-of eDP1 --primary
#feh --bg-fill ~/wallpapers/peaceful_forest_by_bmspire_dec4j13.jpg
wallpapername="night2.jpg"
feh --bg-fill ~/wallpapers/$wallpapername
#killall polybar 
#for m in $(polybar --list-monitors | cut -d":" -f1); do
#    MONITOR=$m polybar --reload bottom &
#    sleep 1
#done
#for m in $(polybar --list-monitors | cut -d":" -f1); do
#        MONITOR=$m polybar --reload top &
#        sleep 1
#done
guake
picom
killall spotifyd
spotifyd --config-path ~/.config/spotifyd/config
