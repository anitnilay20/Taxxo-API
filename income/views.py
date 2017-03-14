from income.serializers import Incomeserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from income.models import Income


class IncomeList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        company = request.META['HTTP_COMPANY']
        income = Income.objects.all()
        serializer = Incomeserializers(income, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Incomeserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Income.objects.get(id=id)
        except Income.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Income = self.get_object(id)
        serializer = Incomeserializers(Income)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Income = self.get_object(id)
        serializer = Incomeserializers(Income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Income = self.get_object(id)
        Income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
