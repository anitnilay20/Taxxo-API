from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from payment import views

urlpatterns = [
    url(r'^$', views.PaymentList.as_view()),
    url(r'^(?P<id>[0-9]+)/$', views.PaymentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)