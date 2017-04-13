from ledgers.models import Ledgers
from ledgers.serializers import Ledgersserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import company


class LedgersList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request):
        company = request.META['HTTP_COMPANY']
        ledgers = Ledgers.objects.filter(company_id=company)
        serializer = Ledgersserializers(ledgers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Ledgersserializers(data=request.data)
        name = request.data['name']
        if Ledgers.objects.filter(name=name).exists():
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LedgersDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Ledgers.objects.get(id=id)
        except Ledgers.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Ledgers = self.get_object(id)
        serializer = Ledgersserializers(Ledgers)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Ledgers = self.get_object(id)
        serializer = Ledgersserializers(Ledgers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Ledgers = self.get_object(id)
        Ledgers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
