#!/bin/sh

value=$(amixer get Capture | grep '\[off\]')

if [ "$value" == "" ]; then
  echo "  ";
else
  echo "%{F#666}  ";
fi
