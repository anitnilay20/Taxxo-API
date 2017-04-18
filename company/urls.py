from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from company import views

urlpatterns = [
    url(r'^$', views.CompanytList.as_view()),
    url(r'^(?P<id>[0-9]+)/$', views.CompanyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

