from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ledgers import views

urlpatterns = [
    url(r'^$', views.LedgersList.as_view()),
    url(r'^(?P<id>[0-9]+)/$', views.LedgersDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)