#!/bin/sh

value=$(bluetoothctl show | grep "Powered: yes" | wc -c)

if [ "$value" == 0 ]
then
  bluetoothctl power on
else
  bluetoothctl power off
fi
