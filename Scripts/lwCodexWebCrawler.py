# implementation based on automatetheboringstuff.com
# this doesn't actually work since lesswrong.com bans scripts
# would need to use selenium

import requests, os, bs4


url = 'https://www.lesswrong.com/s/XsMTxdQ6fprAQMoKi/p/gFMH3Cqw4XxwL69iy' # Scott Alexander's LessWrong Codex
os.makedirs('scott_codex', exist_ok=True)
next_page_exist = True

while next_page_exist:
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    print('Page download in progress: ' + url)

    post = soup.select('.ContentItemBody-root')
    if bool(post):
        postUrl = 'https:' + post[0].get('src')
        res = requests.get(postUrl)
        res.raise_for_status()
        print('Post download in progress: ' + postUrl)
    else:
        print('Post could not be found')

    postFile = open(os.path.join('scott_codex', os.path.basename(postUrl)), 'wb')
    for chunk in res.iter_content(100000):
        postFile.write(chunk)
    postFile.close()

    prevUrl = soup.select('.SequencesNavigationLink-normal')
    if bool(prevUrl):
        prevUrl = prevUrl[0]
        url = 'https://lesswrong.com' + prevUrl.get('href')
    else:
        break