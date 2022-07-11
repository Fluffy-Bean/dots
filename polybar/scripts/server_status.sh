#!/bin/sh

#Script made by Fluffy, use/modify to your needs!
#Twitter: fluffybeanUwU
#Website: gay.fluffybean.gay
#GitHub: Fluffy-Bean

server_list=$(cat ~/.config/polybar/scripts/server_list.txt)
server_status=()

for server in $server_list
do
  ip=$(ping -W 1 -c 1 -4 $server)
  if [ $(echo $ip | grep "1 received" | wc -c) -eq 0 ]
  then
    server_status+=("%{F#666}%{F-}")
  else
    if [ $(echo $ip | grep "0% packet loss" | wc -c) -eq 0 ]
    then
      server_status+=("%{F#B66467}%{F-}")
    else
      server_status+=("")
    fi
  fi
done

if [ $(echo $server_status | wc -c) -eq 0 ]
then
  echo "Error: No servers/IPs in server_list.txt"
else
  echo "${server_status[*]}"
fi
