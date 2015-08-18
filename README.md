# gimmeHumour
reddit scraper that provides a random joke

<hr>

## About
**gimmeHumour** parses [/r/MeanJokes](https://www.reddit.com/r/MeanJokes) (will implement multi-subreddit support in the future) and randomly chooses one joke. 
It then saves the joke to the clipboard, so that it can be pasted wherever.

## Requirements
* `python` (version 3.sumth)
* `xclip`
* `beep`

## Usage
Simply executing `gimmeHumour.sh` will store a joke in your clipboard. You should hear a beep when the the execution is over. If something goes wrong, the joke will be replaced by an error message, which you may choose to debug.

The intended way of executing this script is by binding it to a key sequence. If using [i3-wm](https://i3wm.org/), just add the following lines to your `$HOME/.i3/config`:

```
# save a reddit joke to clipboard
bindsym $mod+j exec /full/path/to/gimmeHumour.sh
```

Now, the whole process is reduced to:
1. Press `$mod+j`.
2. Wait for the beep (should take less than a second).
3. `Ctrl+V` (or `Shift+Insert`) into textbox.
4. **???**
5. Profit.
