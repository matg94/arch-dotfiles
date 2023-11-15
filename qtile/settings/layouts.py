from libqtile.config import Match
from libqtile import layout
from .colors import colors

# Layouts and layout rules


layout_conf = {
    'border_focus': colors['yellow'],
    'border_width': 1,
    'margin': 8,
    'border_radius': 10,
    'active_bg': '#1d2021',
    'active_fg': '#fabd2f',
    'inactive_bg': '#1d2021',
    'inactive_fg': '#fbf1c7',
    'urgent_bg': '#1d2021',
    'urgent_fg': '#fb4934',
    'padding_x': 6,
    'padding_y': 6,
    'bg_color': '#1d2021',
    'font': 'UbuntuMono Nerd Font',
    'fontsize': 12,
    'panel_width': 150,
    'section_fg': '#d65d0e'

}

layouts = [
    layout.MonadTall(**layout_conf),
    layout.TreeTab(**layout_conf)
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='lxappearance'),
        Match(wm_class='ranger'),
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),

    ],
    border_focus=colors['orange']
)
