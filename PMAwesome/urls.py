"""PMContact01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from properties import views as propertiesViews
from messaging import views as messagingViews
from assets import views as assetViews

app_name = 'messaging'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', propertiesViews.property_list, name='index'),
    

    # Messaging ================
    url(r'^message/(?P<pk>\d+)/', messagingViews.message_detail, name='message_detail'),
    url(r'^messages/', messagingViews.message_list, name='message_list'),
    #url(r'^messages/', messagingViews.index, name='message_list'),
    
    url(r'^contact/(?P<pk>\d+)/modal', messagingViews.contact_detail_modal, name='contact_detail_modal'),
    url(r'^contact/(?P<pk>\d+)/', messagingViews.contact_detail, name='contact_detail'),
    url(r'^contacts/', messagingViews.contact_list, name='contact_list'),

    # Properties  ================
    url(r'^property/(?P<pk>\d+)/', propertiesViews.property_detail, name='property_detail'),
    url(r'^property/edit/(?P<pk>\d+)/', propertiesViews.property_edit, name='property_edit'),
    url(r'^property/new/$', propertiesViews.property_new, name='property_new'),
    url(r'^properties/', propertiesViews.property_list, name='property_list'),

    url(r'^lease/(?P<pk>\d+)/modal', propertiesViews.lease_detail_modal, name='lease_detail_modal'),
    url(r'^lease/edit/(?P<pk>\d+)/modal', propertiesViews.lease_edit_modal, name='lease_edit_modal'),
    url(r'^lease/add/(?P<pk>\d+)/modal', propertiesViews.lease_add_modal, name='lease_add_modal'),
    url(r'^lease/(?P<pk>\d+)/', propertiesViews.lease_detail, name='lease_detail'),

    # Assets ================
    url(r'^assets/reserved_keys/', assetViews.reserved_keys, name='reserved_keys'),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]