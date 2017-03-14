from django.test import TestCase
from selenium import webdriver

class PollsTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_create_new_poll_via_admin_site(self):
		#gertrude opens web browser
		self.browser.get(self.live_server_url + '/admin/')

		#sees the 'Django Admin' heading
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.test)

		#ToDo: use the admin site to create a poll
		self.fail('finish this test')


