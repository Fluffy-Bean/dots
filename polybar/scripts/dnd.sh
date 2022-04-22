#!/bin/sh

value=$(gsettings get org.gnome.desktop.notifications show-banners)

if [ $value == "true" ]; then
  #echo "%{F#666}  "   # Icon toggle
  echo ""               # Icon only when do not distrub is on
elif [ $value == "false" ]; then
  echo "  "
fi
