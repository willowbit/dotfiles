#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
#PS1='[\u@\h \W]\$ '
source "$HOME/.cargo/env"

# pfetch
./.welcome.py
bunnyfetch

# export PATH="$HOME/.local/bin:$PATH"
export PS1="\u@\h:[\w] \@ \[$(tput sgr0)\]"
