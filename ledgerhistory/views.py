from ledgerhistory.models import LedgerHistory
from ledgerhistory.serializers import Ledgerhistoryserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LedgerhistoryList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        ledgers = request.META['HTTP_LEDGERS']
        ledgerhistory = LedgerHistory.objects.filter(ledgers_id=ledgers)
        serializer = Ledgerhistoryserializers(ledgerhistory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Ledgerhistoryserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LedgerhistoryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return LedgerHistory.objects.get(id=id)
        except LedgerHistory.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        LedgerHistory = self.get_object(id)
        serializer = Ledgerhistoryserializers(LedgerHistory)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        LedgerHistory = self.get_object(id)
        serializer = Ledgerhistoryserializers(LedgerHistory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        LedgerHistory = self.get_object(id)
        LedgerHistory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
