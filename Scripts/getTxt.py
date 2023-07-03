#! python3
# SOURCE: automatetheboringstuff.com
import requests, sys, pyperclip

if len(sys.argv) > 1:
    link = ''.join(sys.argv[1:])
else:
    link = pyperclip.paste()

res = requests.get(link)
res.raise_for_status()
file = open('file.txt', 'wb')
for chunk in res.iter_content(100000):
    file.write(chunk)
file.close()