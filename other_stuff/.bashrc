#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
#PS1='[\u@\h \W]\$ '
# source "$HOME/.cargo/env"

#./scripts/welcome.py
pfetch
# bunnyfetch
# ./.welcome.py
#neofetch
./scripts/welcome.py


# export PATH="$HOME/.local/bin:$PATH"
export PS1="\u@\h:[\w] \@ \[$(tput sgr0)\]"
export PATH=$HOME/.local/bin:$PATH
export PATH=$HOME/.profile:$PATH
#export TERM=xterm
export XDG_DATA_DIRS=$HOME/:$XDG_DATA_DIRS
export XDG_CURRENT_DESKTOP=kde
