#!/bin/sh

player=$(playerctl -p %any,firefox status)
title=$(playerctl -p %any,firefox metadata --format '{{ title }}')
artist=$(playerctl -p %any,firefox metadata --format '{{ artist }}')

if [ $player = "Playing" ]
then
    if [ "$title" == "" ]
    then
        $title="Unknow title"
    fi
    if [ "$artist" == "" ]
    then
        $artist = "Unknow artist"
    fi
    echo "%{F#151515}%{T2}%{T- F-}%{B#151515}"$title",  "$artist"%{B-}%{F#151515}%{T2}%{T- F-}"
#else
#    echo ""
fi