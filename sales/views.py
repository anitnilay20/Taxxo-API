from sales.models import Sales
from sales.serializers import Salesserializers
from journal.serializers import Journalserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SalesList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        company = request.META['HTTP_COMPANY']
        sales = Sales.objects.filter(company=company)
        serializer = Salesserializers(sales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        response = {}
        journals = request.data['items']
        if not journals:
            return Response("Items Not Found", status=status.HTTP_400_BAD_REQUEST)
        journal_response = []
        for journal in journals:
            serializer = Journalserializers(data=journal)
            if serializer.is_valid():
                serializer.save()
                journal_response.append(serializer.data)
            else:
                journal_response.append(serializer.errors)
                return Response(journal_response, status=status.HTTP_400_BAD_REQUEST)

        sales = request.data['sales']
        sales_response = ''
        serializer = Salesserializers(data=sales)
        serializer.initial_data['journals'] = list(map(lambda keys: keys['id'], journal_response))
        if serializer.is_valid():
            serializer.save()
            sales_response = serializer.data
        else:
            sales_response = serializer.errors
        response['sales'] = sales_response
        response['items'] = journal_response
        return Response(response, status=status.HTTP_201_CREATED)


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
