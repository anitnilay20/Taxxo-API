from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from journal import views

urlpatterns = [
    url(r'^$', views.JournalList.as_view()),
    url(r'^$', views.JournalDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
