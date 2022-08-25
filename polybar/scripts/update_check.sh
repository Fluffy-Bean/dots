#!/bin/sh

value=$(pacman -Qu | wc -l)

if [ "$value" != "0" ]; then
  echo "  ";
else
  echo "";
fi
