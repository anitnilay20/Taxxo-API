from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ledgerhistory import views

urlpatterns = [
    url(r'^$', views.LedgerhistoryList.as_view()),
    url(r'^$', views.LedgerhistoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
