from django.urls import path, re_path

from .views import (
    home_page,
    detail_page,
    month_page,
    create_page,
    home_page_start
    )

urlpatterns = [
    path('', home_page_start, name='home_page_start'),
    path('create/', create_page, name='create_page'),

    re_path('^(?P<slug>[-\w]+)/$', home_page, name='home_page'),
    re_path('^(?P<url>[-\w]+)/detail/(?P<id>\d+)/$', detail_page, name='detail_page'),
    re_path('(?P<url>[-\w]+)/month/(?P<month>[-\w]+)/', month_page, name='month_page'),

]
