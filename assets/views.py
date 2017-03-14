from django.shortcuts import render

from .models import *
from properties.models import Property

# Create your views here.
def reserved_keys(request):
    keys = ReservedKey.objects.all()

    propsWithoutKeys = Property.objects.exclude(pk__in = 
        ReservedKey.objects.values_list('pk', flat=True)
    )

    return render(request, 'reserved_keys.html', {
		'keys': keys, 
        'propsWithoutKeys': propsWithoutKeys,
		'browserTitle': 'Reserved Keys',
		'pageHeader': 'Assets', 
		'breadCrumb1': 'Reserved Keys'
		})
