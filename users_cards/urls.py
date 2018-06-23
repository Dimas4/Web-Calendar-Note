from django.urls import path, re_path

from .views import (
    home,
    create_card,
    card_detail,
    card_add_event,
    card_delete,
    event_finished_delete
    )

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_card, name='create'),

    re_path('^(?P<url>[-\w]+)/$', card_detail, name='card_detail'),
    re_path('^(?P<url>[-\w]+)/delete', card_delete, name='card_delete'),

    re_path('^(?P<url>[-\w]+)/create$', card_add_event, name='card_add_event'),

    re_path('^(?P<url>[-\w]+)/(?P<id>\d+)/(?P<slug>[-\w]+)/delete',
            event_finished_delete,
            name='event_finished_delete'
            ),

]
