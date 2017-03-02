from receipt.models import Receipt
from receipt.serializers import Receiptserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ReceipttList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self,request,format=None):
        company=request.META['HTTP_COMPANY']
        receipt = Receipt.objects.filter(company_id=company)
        serializer = Receiptserializers(receipt, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Receiptserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class  ReceiptDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Receipt.objects.get(id=id)
        except Receipt.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Receipt = self.get_object(id)
        serializer = Receiptserializers(Receipt)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Receipt = self.get_object(id)
        serializer = Receiptserializers(Receipt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Receipt = self.get_object(id)
        Receipt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)