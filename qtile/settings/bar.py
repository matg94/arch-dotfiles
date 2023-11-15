from libqtile import bar, widget, qtile
from .colors import colors

decor = {
    "background": colors['background'],
    "borderwidth": 2,
    "padding": 3,
    "highlight_method": 'text',
    "rounded": "true",
    "disable_drag": True,
    "inactive": colors['current_line'],
    "active": colors['yellow'],
    "highlight_color": colors['blue'],
    "this_current_screen_border": colors['orange'],
    # "block_highlight_text_color": colors['red']
    # "this_screen_border": colors['foreground'],
    # "other_current_screen_border": colors['foreground'],
    # "other_screen_border": colors['foreground'],
    # "this_screen_border": colors['foreground'],

}

left_bar_widgets = [
    widget.Sep(
        linewidth=0,
        padding=5,
        foreground=colors['background'],
        background=colors['background']
    ),
    widget.TextBox(
        text="",
        padding=7,
        fontsize=20,
        foreground=colors['orange'],
        background=colors['background']
    ),
    widget.Sep(
        linewidth=0,
        padding=20,
        foreground=colors['background'],
        background=colors['background']
    ),
    widget.GroupBox(
        **decor,
        font='Red Hat Mono',
        fontsize=12,
    ),
    widget.Sep(
        linewidth=0,
        padding=20,
        foreground=colors['background'],
        background=colors['background']
    ),
    widget.TextBox(
        text='\uE0B0',
        background=colors['current_line'],
        foreground=colors['background'],
        padding=0,
        fontsize=25
    ),
    widget.WindowName(
        padding=5,
        background=colors['current_line'],
        foreground=colors['foreground'],
        empty_group_string="Desktop",
        max_chars=130,
    ),
    widget.TextBox(
        text='\uE0B0',
        background=colors['background'],
        foreground=colors['current_line'],
        padding=0,
        fontsize=25,
    ),
    widget.PulseVolume(
        padding=20,
        background=colors['background'],
        foreground=colors['foreground'],
        fontsize=10,
        limit_max_volume=True,
        scroll_step=10
    ),
    widget.LaunchBar(
        font="JetBrainsMono Bold",
        fontsize=10,
        foreground=colors['foreground'],
        background=colors['background'],
        padding=10,
        progs=[
            ("蓼", "pacmd set-default-sink alsa_output.usb-ACTIONS_Pebble_V3-00.analog-stereo"),
            ("", "pacmd set-default-sink alsa_output.pci-0000_0c_00.4.analog-stereo"),
            ("ﱮ", "thunar"),
            ("", "pavucontrol"),
            ("", "lxappearance")
        ]
    ),
    widget.Clock(
        font="JetBrainsMono Bold",
        fontsize=10,
        foreground=colors['foreground'],
        background=colors['background'],
        format="%B %d %a %H:%M",
        padding=10,
    ),
    widget.Sep(
        linewidth=0,
        padding=5,
        foreground=colors['background'],
        background=colors['background']
    ),
]

right_bar_widgets = [
    widget.Sep(
        linewidth=0,
        padding=5,
        foreground=colors['background'],
        background=colors['background']
    ),
    widget.TextBox(
        text="",
        padding=7,
        fontsize=20,
        foreground=colors['orange'],
        background=colors['background']
    ),
    widget.Sep(
        linewidth=0,
        padding=20,
        foreground=colors['background'],
        background=colors['background']
    ),
    widget.GroupBox(
        **decor,
        font='Red Hat Mono',
        fontsize=12,
    ),
    widget.Sep(
        linewidth=0,
        padding=20,
        foreground=colors['background'],
        background=colors['background']
    ),
    widget.TextBox(
        text='\uE0B0',
        background=colors['current_line'],
        foreground=colors['background'],
        padding=0,
        fontsize=25
    ),
    widget.WindowName(
        padding=5,
        background=colors['current_line'],
        foreground=colors['foreground'],
        empty_group_string="Desktop",
        max_chars=130,
    ),
    widget.TextBox(
        text='\uE0B0',
        background=colors['background'],
        foreground=colors['current_line'],
        padding=0,
        fontsize=25,
    ),
    widget.PulseVolume(
        padding=20,
        background=colors['background'],
        foreground=colors['foreground'],
        fontsize=10,
        limit_max_volume=True,
        scroll_step=10
    ),
    widget.LaunchBar(
        font="JetBrainsMono Bold",
        fontsize=10,
        foreground=colors['foreground'],
        background=colors['background'],
        padding=10,
        progs=[
            ("蓼", "pacmd set-default-sink alsa_output.usb-ACTIONS_Pebble_V3-00.analog-stereo"),
            ("", "pacmd set-default-sink alsa_output.pci-0000_0c_00.4.analog-stereo"),
            ("", "pavucontrol"),
            ("", "lxappearance")
        ]
    ),
    widget.Clock(
        font="Red Hat Mono",
        fontsize=10,
        foreground=colors['foreground'],
        background=colors['background'],
        format="%B %d %a %H:%M",
        padding=10,
    ),
    widget.Sep(
        linewidth=0,
        padding=5,
        foreground=colors['background'],
        background=colors['background']
    )
]

primaryBar = bar.Bar(
    left_bar_widgets,
    24,
    background=colors['current_line'],
    margin=[0, 0, 0, 0],
)

secondaryBar = bar.Bar(
    right_bar_widgets,
    24,
    background=colors['current_line'],
    margin=[0, 0, 0, 0],
)
