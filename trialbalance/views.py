from rest_framework.response import Response
from rest_framework.views import APIView

from trialbalance.models import TrialBalance
from trialbalance.serializers import TrialBalanceSerializers


class TrialBalanceList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        company = request.META['HTTP_COMPANY']
        trialbalance = TrialBalance.objects.filter(company_id=company)
        serializer = TrialBalanceSerializers(trialbalance, many=True)
        return Response(serializer.data)
