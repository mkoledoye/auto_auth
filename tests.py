# write all tests here
import time
import unittest

from edisu_auto_auth import AutoConnect

class UserAlreadyConnected(Exception):
	"""Raise when the client is already connected to the internet"""

	def __init__(self):
		self.message = 'The user is alredy logged in. Please disconnect using the connection window and try again'
		super(UserAlreadyConnected, self).__init__(self.message)


class TestLogin(unittest.TestCase):
	"""Test that client can be logged in automatically"""

	def setUp(self):
		self.retries = 0
		self.connection = AutoConnect(username='moses.koledoye2', password='koomahni')

	def test_login_succeeded(self):
		if not self.connection.is_connected:
			connection.login()
			#wait for server to log user in and grant access
			time.sleep(7)
		else:
			raise UserAlreadyConnected
		self.AssertTrue(self.connection.is_connected)


if __name__ == '__main__':
	unittest.main()

