import os
from libqtile import qtile
from libqtile.config import Key
from libqtile.lazy import lazy

# Qtile keybindings

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "left", lazy.layout.left()),
    ([mod], "right", lazy.layout.right()),
    ([mod], "down", lazy.layout.down()),
    ([mod], "up", lazy.layout.up()),
    ([mod, "shift"], "left", lazy.layout.swap_left()),
    ([mod, "shift"], "right", lazy.layout.swap_right()),
    ([mod, "shift"], "down", lazy.layout.shuffle_down()),
    ([mod, "shift"], "up", lazy.layout.shuffle_up()),
    ([mod], "i", lazy.layout.grow()),
    ([mod], "o", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "space", lazy.window.toggle_floating()),

    # Toggle Fullscreen
    ([mod], "f", lazy.window.toggle_fullscreen()),
    
    # Change Current Screen

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "q", lazy.window.kill()),

    # Switch focus of monitors
    # ([mod], "right", lazy.next_screen()),
    # ([mod], "left", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.reload_config()),
    ([mod, "control", "shift"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),

    # ------------ App Configs ------------


    # Menu
    ([mod], "space", lazy.spawn(os.path.expanduser('rofi -no-lazy-grab -show drun -modi drun -theme ~/.config/rofi/styles/launcher.rasi'))),

    # Window Nav
    (["mod1"], "Tab", lazy.spawn("rofi -show window -theme ~/.config/rofi/styles/show.rasi")),

    # File Explorer
    ([mod], "e", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    # ([mod], "r", lazy.spawn("redshift -O 2400")),
    # ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "p", lazy.spawn("flameshot gui")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

]]

