from sales.models import Sales
from sales.serializers import Salesserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SalesList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        sales = request.meta['HTTP_COMPANY']
        sales = Sales.objects.all(sales=sales)
        serializer = Salesserializers(sales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Salesserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Sales.objects.get(id=id)
        except Sales.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Sales = self.get_object(id)
        serializer = Salesserializers(Sales)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Sales = self.get_object(id)
        serializer = Salesserializers(Sales, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Sales = self.get_object(id)
        Sales.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
