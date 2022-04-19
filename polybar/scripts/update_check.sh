#!/bin/sh

b=$(pacman -Qu | wc -l)

if [[ "$b" -ne "0" ]]; then
  echo "  ";
fi
