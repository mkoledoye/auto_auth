import argparse
import subprocess
import platform

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AutoConnect(object):
	'''
	'''

	def __init__(self, username=None, password=None, snooze=10, expiry=3600*5):
		'''
		'''
		self.uname = username
		self.pwd = password
		self.snz_time = snooze
		# TODO: get default web browser since Chrome may not installed
		self.browser = webdriver.Chrome()


	def is_connected(self, host):
	    """
	    Returns True if host responds to a ping request
	    """
	    win_os_flag = platform.system().lower() == "windows"
	    switch = ("-c", "-n")[win_os_flag]
	    cmd = "ping {} 1 {}".format(switch, host)

	    return subprocess.call(cmd, shell= not win_os_flag) == 0


	def keep_connection_alive(self):
		'''
		'''
		if self.is_connected("www.google.com"):
			time.sleep(self.snz_time)
		else:
			self.login(self.uname, self.pwd)


	def login(self, username, password):
		'''
		'''
		self.browser.get("www.rzim.org")
		
		username = self.browser.find_element_by_id("username")
		password = self.browser.find_element_by_id("password")
		username.send_keys("YourUsername")
		password.send_keys("Pa55worD")

		self.browser.find_element_by_name("submit").click()



