#!/bin/sh

value=$(gsettings get org.gnome.desktop.notifications show-banners)

if [ "$value" == "true" ]; then
  gsettings set org.gnome.desktop.notifications show-banners false
else
  gsettings set org.gnome.desktop.notifications show-banners true
fi
