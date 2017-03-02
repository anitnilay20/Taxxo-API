from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from balance import views

urlpatterns = [
    url(r'^$', views.BalanceList.as_view()),
    url(r'^(?P<id>[0-9]+)/$', views.BalanceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
