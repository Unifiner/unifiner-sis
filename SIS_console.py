from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class SIS_console:
	usr = 0
	pwd = 0
	driver = 0
	url = 'https://sis.rpi.edu/rss/twbkwbis.P_WWWLogin'
	def __init__(self, usr, pwd):
		self.usr = usr
		self.pwd = pwd
		self.driver = webdriver.Chrome()
	def	login(self):
		
		self.driver.get(self.url)
		
		# enter RIN
		usr_input_area = self.driver.find_element_by_id('UserID')
		usr_input_area.send_keys(self.usr)

		# enter password
		pwd_input_area = self.driver.find_element_by_name('PIN')
		pwd_input_area.send_keys(self.pwd)
		pwd_input_area.send_keys(Keys.RETURN)
		
	def capp_report(self):
		self.driver.find_element_by_link_text('Student Menu').click()
		self.driver.find_element_by_link_text('View CAPP Reports').click()
		self.driver.find_element_by_xpath("//body/div/form/input").click()
		
	def add_class(self, CRNs):
		self.driver.find_element_by_link_text('Student Menu').click()
		self.driver.find_element_by_link_text('Register, Add or Drop').click()
		self.driver.find_element_by_xpath("//body/div/form/input").click()
		
#		start to add
		i = 0
		while i < len(CRNs):
			elem_id = 'crn_id' + str(i + 1)
			input_box = self.driver.find_element_by_id(elem_id)
			input_box.send_keys(str(CRNs[i]))
			i += 1
		
		submit_changes = self.driver.find_element_by_xpath('//body/div/form/input[@value="Submit Changes"]')
		submit_changes.click()
		
#		
#CRN = [11111, 22222, 33333]  # Enter the CRNs of the courses
#
#user = input('Please enter your RIN here ==> ')  # Enter your RIN here
#pwd = input('Please enter your password here ==> ')   # Enter your password here
#
#
#input('When you are ready, press ENTER to start')
#
## open chrome and goto the sis login page
#driver = webdriver.Chrome()
#driver.get(url)
#
#
#
#
## goto register, add, or drop (rad) menu
#rad = driver.find_element_by_link_text('Register, Add or Drop')
#rad.click()
#
## select semester from dropdown <select>
#semester = Select(driver.find_element_by_id('term_id'))
#semester.select_by_visible_text('Fall 2018')  # TODO: change to Spring 2019
#submit_button = driver.find_element_by_xpath("//body/div/form/input")  # submit the request
#submit_button.click()
#
## input CRNs
#i = 0
#while i < len(CRN):
#	elem_id = 'crn_id' + str(i + 1)
#	input_box = driver.find_element_by_id(elem_id)
#	input_box.send_keys(str(CRN[i]))
#	i += 1
#
#submit_changes = driver.find_element_by_xpath('//body/div/form/input[@value="Submit Changes"]')
#submit_changes.click()