#! python3
# mapIt.py - Launches a map in the browser from an address in cmd line or clipboard
# SOURCE: automatetheboringstuff.com

import webbrowser, sys, pyperclip

if len(sys.argv) > 1: # if cmd line has more than just the filename, len(..) > 1
    # Get address from cmd line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)