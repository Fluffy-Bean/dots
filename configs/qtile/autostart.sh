#!/bin/sh
xrandr --output HDMI-0 --mode 1920x1080 --rate 144 &                    # 144hz
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &             # polkit

picom --experimental-backends -b &                                      # compositor
nitrogen --restore &                                                    # wallpaper
eww open bar &                                                          # bar
~/.config/eww/scripts/workspaces &                                      # workspaces for bar

amixer -q sset Master 100% &                                            # set volume 100%
flameshot &                                                             # screenshot tool
dunst &                                                                 # notification daemon

curl -s "http://lamp.box/cm?cmnd=Power%20On" &                          # turn on lamp
openvpn3 session-start --config /etc/openvpn/client/nl-04.udp.ovpn &    # start proton vpn