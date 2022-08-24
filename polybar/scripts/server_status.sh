#!/bin/sh

## Script made by Fluffy, use/modify to your needs!
## Twitter: fluffybeanUwU
## Website: gay.fluffybean.gay
## GitHub: Fluffy-Bean

if [ $(cat ~/.config/polybar/scripts/server_list.txt | wc -c) == 0 ]
then
  echo "Error: No Servers/IPs in server_list.txt"
else
  server_list=$(cat ~/.config/polybar/scripts/server_list.txt)
  server_status=()

  for server in $server_list
  do
    ip=$(ping -W 1 -c 3 -4 $server)
    if [ $(echo $ip | grep "0 received" | wc -l) == 1 ]
    then
      server_status+=("%{F#666}%{F-}")
    else
      if [ $(echo $ip | grep ", 0% packet loss" | wc -l) == 0 ]
      then
        server_status+=("%{F#B66467}%{F-}")
      else
        server_status+=("")
      fi
    fi
  done

  if [ $(echo $server_status | wc -c) == 0 ]
  then
    echo "Error: Could not add pinged servers"
  else
    echo "${server_status[*]}"
  fi
fi
