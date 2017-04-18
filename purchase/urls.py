from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from purchase import views

urlpatterns = [
    url(r'^$', views.PurchaseList.as_view()),
    url(r'^$', views.PurchaseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
