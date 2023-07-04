# implementation based on automatetheboringstuff.com
# selenium crawl of lesswrong codex
# will open a browser tab

# i got rate limited while testing :sob:

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.lesswrong.com/s/XsMTxdQ6fprAQMoKi/p/gFMH3Cqw4XxwL69iy')

text_file = open("/Users/Chenster/py/scott_codex.txt", "a") # replace with your own user path

counter = 0
while counter < 150: # 150 pages is a hard ceiling
    counter+=1
    try:
        elemCheck = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ContentItemBody-root'))
        )
    finally:
        try:
            title = browser.find_element(By.CSS_SELECTOR, '.PostsPageTitle-link')
            elem = browser.find_element(By.CSS_SELECTOR, '.ContentItemBody-root')
            print('downloading page ' + str(counter) + '...')
            n = text_file.write('\n\n\n\n\n\n\n' + str(title.text) + '\n\n\n\n' + str(elem.text))
        except Exception as e:
            print("couldn't find element")
            print(e)
        
        try:
            linkNext = browser.find_elements(By.CSS_SELECTOR, '.SequencesNavigationLink-normal')
            if linkNext[-1] == linkNext[0]: # need to fix this
                break
            else:
                linkNext[-1].click()
        except:
            print("couldn't find next link")

text_file.close()
browser.quit()



