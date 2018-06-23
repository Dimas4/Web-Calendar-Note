from django.urls import path, re_path

from .views import (
    home_page,
    detail_page
    )

urlpatterns = [
    path('', home_page, name='home_page'),
    re_path('^detail/(?P<pk>\d+)/(?P<id>\d+)/$', detail_page, name='detail_page'),
    # re_path('(?P<id>\d+)/', home_page, name='home_page'),

]
