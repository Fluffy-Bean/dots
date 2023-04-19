# ----------------------------------------
#  Importing
# ----------------------------------------
#  Used to control windows and window
#  placement
from libqtile.command import lazy
from libqtile.config import EzKey, EzDrag, EzClick
import os

@lazy.window.function
def float_to_front(window):
    if window.floating:
        window.cmd_bring_to_front()


# ----------------------------------------
#  Default apps
# ----------------------------------------
#  I mostly use Rofi to launch apps so not
#  too important to me
TERMINAL = "alacritty"
SCREENSHOT = "flameshot gui"
LAUNCHER = "rofi -show drun\
    -theme-str '#window {\
        anchor: center; location: center;\
        y-offset: 0; x-offset: 0;\
    }'"
BROWSER = "firefox"


# ----------------------------------------
#  Modifier keys
# ----------------------------------------
#  Used to move and control window
#  placement within Qtile
EzKey.modifier_keys = {
    "M": "mod4",    # Windows
    "A": "mod1",    # Alt
    "S": "shift",   # Shift
    "C": "control", # Ctrl
}


# ----------------------------------------
#  Mouse
# ----------------------------------------
#  Controling floating windows with a
#  mouse
mouse = [
    EzDrag(
        "M-<Button1>",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    EzDrag(
        "M-<Button3>", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    EzClick("M-<Button2>", lazy.window.bring_to_front()),
]


# ----------------------------------------
#  Window
# ----------------------------------------
#  Different lists of window controls for
#  Qtile
window_navigation = [
    EzKey("M-<Tab>", lazy.group.next_window(), float_to_front()),
    EzKey("M-<Left>", lazy.layout.left()),
    EzKey("M-<Down>", lazy.layout.down()),
    EzKey("M-<Up>", lazy.layout.up()),
    EzKey("M-<Right>", lazy.layout.right()), 
]

window_displacement = [
    EzKey("M-C-<Left>", lazy.layout.swap_left(), lazy.layout.shuffle_left()),
    EzKey("M-C-<Down>", lazy.layout.swap_down(), lazy.layout.shuffle_down()),
    EzKey("M-C-<Up>", lazy.layout.swap_up(), lazy.layout.shuffle_up()),
    EzKey("M-C-<Right>", lazy.layout.swap_right(), lazy.layout.shuffle_right()),
]

window_dimension = [
    EzKey("M-S-<Left>", lazy.layout.grow()),
    EzKey("M-S-<Right>", lazy.layout.shrink()),
    EzKey("M-S-<Tab>", lazy.layout.reset()),
]

window_toggles = [
    EzKey("M-y", lazy.next_layout()),
    EzKey("M-q", lazy.window.kill()),
    EzKey("M-g", lazy.window.toggle_floating()),
    EzKey("M-m", lazy.window.toggle_fullscreen()),
]


# ----------------------------------------
#  Qtile and App
# ----------------------------------------
#  Launching apps and qtile settings
qtilectl = [
    EzKey("M-S-r", lazy.restart()),
    EzKey("M-S-q", lazy.shutdown()),
    EzKey("M-L", lazy.spawn("dm-tool lock")),
]

rofi = [
    EzKey("M-r", lazy.spawn(LAUNCHER)),
]

application_spawns = [
    EzKey("M-t", lazy.spawn(TERMINAL)),
    EzKey("M-b", lazy.spawn(BROWSER)),
]

mediactl = [
    EzKey("<XF86AudioPlay>", lazy.spawn("playerctl play-pause -i firefox")),
    EzKey("<XF86AudioNext>", lazy.spawn("playerctl next -i firefox")),
    EzKey("<XF86AudioPrev>", lazy.spawn("playerctl previous -i firefox")),
]

volumectl = [
    EzKey("<XF86AudioRaiseVolume>", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    EzKey("<XF86AudioLowerVolume>", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    EzKey("<XF86AudioMute>", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    EzKey("M-f", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/toggle_mic"))),
]

scrcap = [
    EzKey("<Print>", lazy.spawn(SCREENSHOT)),
]


# ----------------------------------------
#  Keybinds
# ----------------------------------------
#  Putting all keybinds into one list to
#  use in other scripts
keys = [
    *window_navigation,
    *window_displacement,
    *window_dimension,
    *window_toggles,
    *qtilectl,
    *rofi,
    *application_spawns,
    *mediactl,
    *volumectl,
    *scrcap,
]