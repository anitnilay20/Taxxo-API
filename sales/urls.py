from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from sales import views

urlpatterns = [
    url(r'^$', views.SalesList.as_view()),
    url(r'^$', views.SalesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
