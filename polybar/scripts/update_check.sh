#!/bin/sh

b=$(pacman -Qu | wc -l)

if [ "$b" != "0" ]; then
  echo "  ";
else
  echo "";
fi
