#!/bin/sh
nitrogen --restore &
picom --experimental-backends -b &
xrandr --output HDMI-0 --mode 1920x1080 --rate 144 &
polybar -r fluffy &
flameshot &
dunst &