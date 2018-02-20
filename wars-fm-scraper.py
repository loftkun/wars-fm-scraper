#!/usr/bin/env python3

import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# args
if( len(sys.argv) != 3 ):
	print('usage : wars-fm-scraper.py url filepath')
	sys.exit()
url		= sys.argv[1] # http://wars.fm/shogi10?gameId=r0jo2gocc27f#game/r0jo2gocc27f
filepath= sys.argv[2] # test.csa

# driver
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=options)

# get page
print('get : {}'.format(url))
driver.get(url)
try:
	# wait #export-button visible
	# https://kurozumi.github.io/selenium-python/waits.html
	#print('wait export-button start')
	WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.ID, "export-button")))
	#print('wait export-button end')
except:
	# timeout
	print('wait export-button timeout')
	sys.exit()

# HTML source
#print(driver.page_source)

# screenshot
#driver.set_window_size(1280, 720) 
#FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screen.png")
#driver.save_screenshot(FILENAME)

# click export-button
#print('click export-button start')
driver.find_element_by_id("export-button").click()
#print('click export-button end')

try:
	# wait #kif-export-box visible
	#print('wait kif-export-box start')
	WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.ID, "kif-export-box")))
	#print('wait kif-export-box end')
except:
	# timeout
	print('wait kif-export-box timeout')
	sys.exit()


# get kif string
kif = driver.find_element_by_id("kif-export-box").get_attribute('value')
#print(kif)

# save kif
f = open(filepath, 'w')
f.write(kif)
f.close()
print('saved : {}'.format(filepath))

# close driver
driver.quit()
