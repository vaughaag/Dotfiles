#!/bin/sh

function run {
  if ! pgrep $1 ;
  then
    $@&
  fl
}

xrandr --output DisplayPort-0 --mode 1920x1200 --pos 3840x0 --rotate normal --output DisplayPort-1 --mode 1920x1200 --pos 0x0 --rotate normal --output DisplayPort-2 --primary --mode 1920x1200 --pos 1920x0 --rotate normal --output HDMI-A-0 --off --output DVI-D-0 --off

run nm-applet
run pamac-tray
run blueberry-tray
run numlock on
run volumeicon
run /usr/lib/polkit-gnome/polkit=gnome-authentication-agent-1
