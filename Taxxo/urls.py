from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
                  url(r'^company/', include('company.urls')),
                  url(r'^customer/', include('Customer.urls')),
                  url(r'^ledgers/', include('ledgers.urls')),
                  url(r'^activity/', include('activity.urls')),
                  url(r'^journal/', include('journal.urls')),
                  url(r'^admin/', include('admin.site.urls')),
                  url(r'^purchase/', include('purchase.urls')),
                  url(r'^sales/', include('sales.urls')),
                  url(r'^ledgerhistory/', include('ledgerhistory.urls')),
                  url(r'^product/', include('product.urls')),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
