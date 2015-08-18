#!/bin/bash

# Run the script and save the output to clipboard
python /home/sergiu/work/gimmeHumour/main.py | xclip -selection clipboard

# Beep to know when it's done
beep

# Just Ctrl+V (or Shift+Insert) to paste the joke wherever.
