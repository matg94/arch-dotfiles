# Qtile workspaces

from libqtile.config import Key, Group, Match
from libqtile.lazy import lazy
from .keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons:
# nf-fa-firefox,
# nf-fae-python,
# nf-dev-terminal,
# nf-fa-code,
# nf-oct-git_merge,
# nf-linux-docker,
# nf-mdi-image,
# nf-mdi-layers

# Groups
groups = [
    Group(name='1', label=""),
    Group(name='2', label=""),
    Group(name='3', label=""),
    Group(name='4', label=""),
    Group(name='5', label="")
]


for index, group in enumerate(groups):
    keys.extend([
        Key([mod], group.name, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name)),
    ])
