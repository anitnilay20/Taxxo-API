from django.contrib import admin
from django.conf.urls import url, include
import company

urlpatterns = [
    url(r'^user/', admin.site.urls),
    url(r'^company/', include('company.urls')),
    url(r'^customer/', include('Customer.urls')),
    url(r'^balance/', include('balance.urls')),
    url(r'^contra/', include('contra.urls')),
    url(r'^ledgers/', include('ledgers.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^receipt/', include('receipt.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
