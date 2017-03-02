from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from contra import views

urlpatterns = [
    url(r'^$', views.ContraList.as_view()),
    url(r'^(?P<id>[0-9]+)/$', views.ContraDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)