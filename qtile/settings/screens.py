import os
from libqtile import bar, widget, qtile
from libqtile.config import Screen

from .bar import primaryBar, secondaryBar

screens = [
    Screen(
            top=primaryBar,
        ),
    Screen(
            top=secondaryBar,
        )
]
