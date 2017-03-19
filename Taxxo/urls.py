from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^user/', admin.site.urls),
    url(r'^company/', include('company.urls')),
    url(r'^customer/', include('Customer.urls')),
    url(r'^balance/', include('balance.urls')),
    url(r'^contra/', include('contra.urls')),
    url(r'^ledgers/', include('ledgers.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^expense/', include('expense.urls')),
    url(r'^income/', include('income.urls')),
    url(r'^receipt/', include('receipt.urls')),
    url(r'^activity/', include('activity.urls')),
    url(r'^trialbalance/', include('trialbalance.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
