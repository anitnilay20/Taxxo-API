from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from trialbalance import views

urlpatterns = [
    url(r'^$', views.TrialBalanceList.as_view()),
    url(r'profitloss/',views.ProfitLoss.as_view()),
    url(r'balancesheet/',views.Balancesheet.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
