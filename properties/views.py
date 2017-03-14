from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import *

import datetime

# import model
from .models import *
from assets.models import ReservedKey


def index(request):
    return HttpResponse('Property Dashboard')


def property_list(request):
    today = datetime.datetime.now()

    propFilter = Q(archived_on=None) | Q(archived_on__gt=today)  # remove any archived results
    if (request.GET.get('showArchived') == '1'):
        propFilter = Q(archived_on__lte=today)  # remove any archived results

    properties = Property.objects.filter(propFilter).order_by('-created_on')[:100]

    # alerts
    rangeStart = today - datetime.timedelta(days=(30 * 2))
    rangeEnd = today + datetime.timedelta(days=(30 * 4))
    propActivities = PropertyActivity.objects.filter(activity_on__gte=rangeStart, activity_on__lte=rangeEnd,
                                                     priority__gte=PropertyActivity.PRIORITY_LOW).only('prop', 'type',
                                                                                                       'priority',
                                                                                                       'activity_on').order_by(
        '-activity_on')

    return render(request, 'property_list.html', {
        'properties': properties,
        'propActivities': propActivities,
        'browserTitle': 'Properties List',
        'pageHeader': 'Properties',
        'breadCrumb1': 'Property List'
    })


def property_detail(request, pk):
    prop = get_object_or_404(Property, pk=pk)

    leaseHistory = prop.lease_set.order_by('-dateLeaseStart')

    owners = prop.propertyowner_set.order_by('-percentageShare')
    currentLease = prop.currentLease()

    if currentLease is not None:
        leaseContacts = currentLease.leasecontact_set.exclude(type=LeaseContact.TYPE_OWNER).order_by('-type',
                                                                                                     'contact__nameFirst')
    else:
        leaseContacts = None

    propActivities = PropertyActivity.objects.filter(prop=pk, priority__gte=PropertyActivity.PRIORITY_LOG).order_by(
        '-activity_on')

    try:
        resKey = prop.reservedkey
    except ReservedKey.DoesNotExist:
        resKey = None

    # import pdb; pdb.set_trace()


    return render(request, 'property_detail.html', {
        'prop': prop,
        'resKey': resKey,
        'leaseHistory': leaseHistory,
        'currentLease': currentLease,
        'owners': owners,
        'contacts': leaseContacts,
        'propActivities': propActivities,
        'browserTitle': prop.name + ': Property Details',
        'pageHeader': prop.name,
        'breadCrumb1': 'Property List',
        'breadCrumb2': 'Property Detail'
    })


def property_new(request):
    if request.method == 'POST':
        form = PropForm(request.POST)
        # return HttpResponse(form)
        if form.is_valid():
            # process the data in form.cleaned_data
            form.save()
            # redirect to detail page
            return HttpResponseRedirect('/properties')

    else:
        form = PropForm()

    return render(request, 'property_edit.html', {
        'form': form,
        'browserTitle': 'Creating New Property',
        'pageHeader': 'Creating New Property',
        'breadCrumb1': 'Property List',
        'breadCrumb2': 'Property New',
    })


def property_edit(request, pk):
    prop = get_object_or_404(Property, pk=pk)

    if request.method == 'POST':

        form = PropForm(request.POST, instance=prop)
        # return HttpResponse(form)
        if form.is_valid():
            # process the data in form.cleaned_data
            form.save()
            # redirect to detail page
            return HttpResponseRedirect('/property/'+ prop.id.__str__())

    else:
        form = PropForm(instance=prop)

    return render(request, 'property_edit.html', {
        'form': form,
        'prop': prop,
        'browserTitle': 'Editing ' + prop.name,
        'pageHeader': prop.name,
        'breadCrumb1': 'Property List',
        'breadCrumb2': 'Property Edit',
    })


def lease_detail(request, pk):
    lease = get_object_or_404(Lease, pk=pk)

    return render(request, 'lease_detail.html', {
        'browserTitle': 'Lease Editing',
        'pageHeader': lease.prop,
        'lease': lease
    })

def lease_detail_modal(request, pk):
    lease = get_object_or_404(Lease, pk=pk)

    return render(request, 'lease_detail_modal.html', {
        'browserTitle': 'Lease Editing',
        'pageHeader': lease.prop,
        'lease': lease
    })

def lease_add_modal(request, pk):
    prop = get_object_or_404(Property, pk=pk)

    if request.method == 'POST':
        form = LeaseForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/property/'+ prop.id.__str__())
    else:
        form = LeaseForm()

    return render(request, 'lease_add_modal.html', {
        'pageHeader': 'Add a New Lease',
        'form': form,
        'prop': prop,
    })



def lease_edit_modal(request, pk):
    lease = get_object_or_404(Lease, pk=pk)

    if request.method == 'POST':
        form = LeaseForm(request.POST, instance=lease)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/property/'+ lease.prop_id.__str__())
    else:
        form = LeaseForm(instance=lease)

    return render(request, 'lease_edit_modal.html', {
        'form': form,
        'pageHeader': 'Edit This Lease',
    })


