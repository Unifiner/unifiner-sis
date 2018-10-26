from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class SIS_console:
	usr = 0
	pwd = 0
	driver = 0
	url = 'https://sis.rpi.edu/rss/twbkwbis.P_WWWLogin'
	def __init__(self, usr = 0, pwd = 0):
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
#		TODO FIGURE OUT HOW TO DOWNLOAD A PDF OF THE PAGE FOR CAPP REPORT
		if input("Enter (y|n) for whether you want your CAPP Report downloaded!") == "y":
			target_path = input("Enter your path which of your file will be downloaded to:")
			self.driver.save_screenshot('capp_report.png')
			self.driver.save_screenshot(target_path)
		
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