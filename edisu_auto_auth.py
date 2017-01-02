import argparse
import subprocess
import platform
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def _get_browser(platform):
	if platform == "windows":
		pass # use IE or edge as browser

	return webdriver.Chrome()


class AutoConnect(object):
	""" 	"""

	def __init__(self, username='', password='', snooze=7, expiry=3600*5):
		"""
		"""
		self.uname = username
		self.pwd = password
		self.snooze_time = snooze
		# TODO: get default web browser since Chrome may not be installed
		self.browser = _get_browser(self.platform)
		self.test_host = "www.yahoo.com"
		self._last_connected = None
		
	@property
	def is_connected(self):
		"""
		Returns True if host responds to a ping request
		"""
		win_os_flag = self.platform == "windows"
		switch = ("-c", "-n")[win_os_flag]
		cmd = ["ping", switch, "1", self.test_host]
		return subprocess.call(cmd) == 0

	@property
	def platform(self):
		return platform.system().lower()

	def keep_connection_alive(self):
		"""
		"""
		if not self.is_connected(self.test_host):
			success = self.login(self.uname, self.pwd)
			if success:
				self.deep_sleep()
		# sleep for ten  seconds before trying again
		time.sleep(10)

	def login(self):
		"""
		"""
		self.browser.get("http://{}".format(self.test_host))
		
		username = self.browser.find_element_by_name("U")
		password = self.browser.find_element_by_name("P")
		username.send_keys(self.uname)
		password.send_keys(self.pwd)

		form = self.browser.find_element_by_name("data")
		form.submit()
		time.sleep(7)
		# check if login succeeded
		if self.is_connected:
			self._last_connected = datetime.now()
			return True
		return False
			

	def deep_sleep(self):
		print('Going to sleep...')
		time.sleep(60*55)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--username", required=True, help = "username for authentication")
	#this password can be entered in plain text since it poses no security risk
	parser.add_argument("-p", "--password", required=True, help = "password for authentication")
	args = parser.parse_args()
	connection = AutoConnect(**vars(args))
	while True:
		connection.keep_connection_alive()



