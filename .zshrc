# If you come from bash you might have to change your $PATH.
export PATH=$HOME/.local/bin:$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="refined"

plugins=(git)

source $ZSH/oh-my-zsh.sh


export MOZ_ENABLE_WAYLAND=1
export GTK_THEME=Nordic-master
export QT_STYLE_OVERRIDE=Nordic-master
source <(kubectl completion zsh)
