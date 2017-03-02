from balance.models import Balance
from balance.serializers import Balanceserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BalanceList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        company = request.META['HTTP_COMPANY']
        balance = Balance.objects.filter(company_id=company)
        serializer = Balanceserializers(balance, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Balanceserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BalanceDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Balance.objects.get(id=id)
        except Balance.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Balance = self.get_object(id)
        serializer = Balanceserializers(Balance)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Balance = self.get_object(id)
        serializer = Balanceserializers(Balance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Balance = self.get_object(id)
        Balance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
