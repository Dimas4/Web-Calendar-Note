from django.urls import path, re_path

from .views import (
    edit_page,
    home_page,
    month_page,
    detail_page,
    create_page,
    create_event,
    home_page_start,
    event_finished_delete
    )

urlpatterns = [
    path('', home_page_start, name='home_page_start'),
    path('create/', create_page, name='create_page'),

    re_path('^(?P<slug>[-\w]+)/$', home_page, name='home_page'),
    path('', home_page, name='home_page'),

    re_path('^(?P<url>[-\w]+)/detail/(?P<id>\d+)/$', detail_page, name='detail_page'),

    re_path('^(?P<url>[-\w]+)/detail/(?P<id>\d+)/create_event$', create_event, name='create_event'),
    re_path('^(?P<url>[-\w]+)/detail/(?P<id>\d+)/edit$', edit_page, name='edit_page'),

    re_path('(?P<url>[-\w]+)/month/(?P<month>[-\w]+)/', month_page, name='month_page'),

    re_path('^(?P<url>[-\w]+)/detail/(?P<id>\d+)/(?P<slug>[-\w]+)',
            event_finished_delete,
            name='event_finished_delete'
            ),


]
