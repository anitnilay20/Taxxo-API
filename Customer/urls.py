from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Customer import views

urlpatterns = [
    url(r'^login/', views.CustomerLogin.as_view()),
    url(r'^$', views.CustomerList.as_view()),
    url(r'^(?P<id>[0-9]+)/$', views.CustomerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)