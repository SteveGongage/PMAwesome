from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

import datetime
import sys

# import model
from .models import Message, Contact, Thread
from properties.models import PropertyOwner, LeaseContact


def message_list(request):
	latestMessages = Message.objects.order_by('-created_on')[:100]
	return render(request, 'message_list.html', {
		'messages': latestMessages,
		'browserTitle': 'Messages',
		'pageHeader': 'Messages', 
		'breadCrumb1': 'Messages'
		})


def message_detail(request, pk):
	message = Message.objects.get(id=pk)
	message.markAsRead()
	return render(request, 'message_detail.html', {
		'message': message,
		'browserTitle': 'Messages',
		'pageHeader': 'Messages', 
		'breadCrumb1': 'Messages'
		})


def contact_list(request):
	return render(request, 'contact_list.html', {
		'browserTitle': 'Contacts',
		'pageHeader': 'Contacts', 
		'breadCrumb1': 'Contacts'
		})


def contact_detail(request, pk):
	contact = Contact.objects.get(id=pk)

	propsOwned = PropertyOwner.objects.filter(contact_id = pk)

	

	return render(request, 'contact_detail.html', {
		'contact': contact,
		'propsOwned': propsOwned,
		'browserTitle': 'Contact Details',
		'pageHeader': 'Contact Details', 
		'breadCrumb1': 'Contacts',
		'breadCrumb1': 'Contact Details'
		})


def contact_detail_modal(request, pk):
	contact = Contact.objects.get(id=pk)

	propsOwned = PropertyOwner.objects.filter(contact_id = pk)

	return render(request, 'contact_detail_modal.html', {
		'contact': contact,
		'propsOwned': propsOwned,
		'browserTitle': 'Contact Details',
		'pageHeader': 'Contact Details', 
		'breadCrumb1': 'Contacts',
		'breadCrumb1': 'Contact Details'
		})
