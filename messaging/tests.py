import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Message

class MessageMethodTests(TestCase):
	#def test_message_model_exists(self):


	def test_message_was_created_recently(self):
		"""
		was_created_recently() should return True if created in last 3 days, otherwise false
		"""
		time = timezone.now() + datetime.timedelta(days=1)
		future_message = Message(created_on=time)
		self.assertIs(future_message.was_created_recently(), False, "Created date is 1 day in the future")

		time = timezone.now() - datetime.timedelta(days=4)
		past_message = Message(created_on=time)
		self.assertIs(past_message.was_created_recently(), False, "Created date is 4 days in the past.")

		time = timezone.now() - datetime.timedelta(days=3)
		past_message = Message(created_on=time)
		self.assertIs(past_message.was_created_recently(), True, "Created date is 3 days in the past.")


		#myMessage = Message.objects.all()
		#self.assertIsNot(len(myMessage), 0, 'Should return at least one result')
		#self.assertIs(myMessage[0].fromName(), '')


