import argparse
import subprocess
import platform
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AutoConnect(object):
	'''
	'''

	def __init__(self, username='', password='', snooze=7, expiry=3600*5):
		'''
		'''
		self.uname = username
		self.pwd = password
		self.snz_time = snooze
		# TODO: get default web browser since Chrome may not be installed
		self.browser = webdriver.Chrome()
		self.test_host = "www.yahoo.com"
		self._last_connected = None
		

	@property
	def is_connected(self):
		"""
		Returns True if host responds to a ping request
		"""
		win_os_flag = platform.system().lower() == "windows"
		switch = ("-c", "-n")[win_os_flag]
		cmd = ["ping", switch, "1", self.test_host]
		status = subprocess.call(cmd) == 0
		return status


	def keep_connection_alive(self):
		'''
		'''
		if self.is_connected(self.test_host):
			time.sleep(self.snz_time)
		else:
			self.login(self.uname, self.pwd)


	def login(self):
		'''
		'''
		self.browser.get("http://{}".format(self.test_host))
		
		username = self.browser.find_element_by_name("U")
		password = self.browser.find_element_by_name("P")
		username.send_keys(self.uname)
		password.send_keys(self.pwd)

		form = self.browser.find_element_by_name("data")
		form.submit()
		time.sleep(7)

		if self.is_connected:
			self._last_connected = datetime.now()
			self.deep_sleep()

	def deep_sleep(self):
		pass


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--username", required=True, help = "username for authentication")
	#this password can be entered in plain text since its issued by network admins, isn't modifiable and does not permit simultaneous login
	parser.add_argument("-p", "--password", required=True, help = "password for authentication")
	args = parser.parse_args()
	connection = AutoConnect(**vars(args))
	while True:
		connection.keep_connection_alive()



