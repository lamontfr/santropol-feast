from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from member.views import *

urlpatterns = patterns(
    '',
    url(_(r'^list/$'),
        ClientList.as_view(), name='list'),
    url(_(r'^notes/$'),
        NoteList.as_view(), name='notes'),
    url(_(r'^note/read/(?P<id>[0-9]{1})/$'),
        mark_as_read, name='read'),
)
