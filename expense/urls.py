from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from expense import views

urlpatterns = [
    url(r'^$', views.ExpenseList.as_view()),
    url(r'^(?P<id>[0-9]+)/$', views.ExpenseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)