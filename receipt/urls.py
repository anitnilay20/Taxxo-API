from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from receipt import views

urlpatterns = [
    url(r'^$', views.ReceipttList.as_view()),
    url(r'^(?P<id>[0-9]+)/$', views.ReceiptDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)