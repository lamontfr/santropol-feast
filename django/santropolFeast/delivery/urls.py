from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from delivery.views import Orderlist, MealInformation, RoutesInformation
from delivery.views import kcr_view

urlpatterns = [
    url(_(r'^order/$'), Orderlist.as_view(), name='order'),
    url(_(r'^meal/$'), MealInformation.as_view(), name='meal'),
    url(_(r'^route/$'), RoutesInformation.as_view(), name='route'),
    url(_(r'^kitchen_count/$'), kcr_view, name='route')
]
