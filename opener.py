from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import sys
import argparse


#	example:
#		go to menue of 'Student Menu' followed by submenu of 'View Grades'
#			opener.open(driver, menu='Student Menu', submenu='View Grades')
#		if submenu is empty, it stops after the menu is opened
def open(driver, menu='', submenu=''):
	if menu == '': return
	if submenu == '':
		driver.find_element_by_link_text(menu).click()
	else:
		driver.find_element_by_link_text(menu).click()
		try:
			driver.find_element_by_xpath(f'//td[@class="mpdefault"]/a[text()="{submenu}"]').click()
		except:
			driver.find_element_by_link_text(submenu).click()
	