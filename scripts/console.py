from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import sys
import argparse

import opener

def	login(driver, url, usr, pwd):
	
	driver.get(url)
	
	# enter RIN
	usr_input_area = driver.find_element_by_id('UserID')
	usr_input_area.send_keys(usr)

	# enter password
	pwd_input_area = driver.find_element_by_name('PIN')
	pwd_input_area.send_keys(pwd)
	pwd_input_area.send_keys(Keys.RETURN)
	
def capp_report(driver):
	driver.find_element_by_link_text('Student Menu').click()
	driver.find_element_by_link_text('View CAPP Reports').click()
	driver.find_element_by_xpath("//body/div/form/input").click()

	#	TODO FIGURE OUT HOW TO DOWNLOAD A PDF OF THE PAGE FOR CAPP REPORT
	if input("Enter (y|n) for whether you want your CAPP Report downloaded!") == "y":
		target_path = input("Enter your path which of your file will be downloaded to:")
		driver.save_screenshot('capp_report.png')
		driver.save_screenshot(target_path)
	
def add_class(driver, crns):
	opener.open(driver, 'Student Menu', 'Register, Add or Drop')
	driver.find_element_by_xpath("//body/div/form/input").click()

	#	start to add
	i = 0
	while i < len(crns):
		elem_id = 'crn_id' + str(i + 1)
		input_box = driver.find_element_by_id(elem_id)
		input_box.send_keys(crns[i])
		i += 1
	
	submit_changes = driver.find_element_by_xpath('//body/div/form/input[@value="Submit Changes"]')
	submit_changes.click()

def auto_time_sheet(driver, timesheet):
	driver.find_element_by_link_text('HR/Payroll Menu').click()
	driver.find_element_by_link_text('Time Sheet').click()
	
	currentPeriod = driver.find_element_by_id('period_1_id').find_element_by_css_selector('option:first-child')
	if not 'Not Started' in currentPeriod.text:
		timesheet_open = driver.find_element_by_xpath('//body/div/form/table/tbody/tr/td/input[@value="Time Sheet"]')
		timesheet_open.click()

def parseParameter():
	
	# set up arg parser
	parser = argparse.ArgumentParser()
	parser.add_argument('--usr', '-u', dest='usr', required=True)
	parser.add_argument('--pwd', '-p', dest='pwd', required=True)
	parser.add_argument('--add-class', '-ac', nargs='*', dest='crns')
	parser.add_argument('--auto-time-sheet', '-ats', nargs='*', dest='timesheet')
	
	# parsing args
	args = parser.parse_args(sys.argv[1:])
	
	return args

def main():
	driver = webdriver.Chrome()
	url = 'https://sis.rpi.edu/rss/twbkwbis.P_WWWLogin'

	# parse command line arguments
	arguments = parseParameter()

	login(driver, url, arguments.usr, arguments.pwd)
	
#	capp_report(driver)
	
	add_class(driver, arguments.crns)
	
#	auto_time_sheet(driver, arguments.timesheet)
	input()
	
if __name__ == "__main__": main()