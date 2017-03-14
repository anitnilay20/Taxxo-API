from expense.serializers import Expenseserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from expense.models import Expense


class ExpenseList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        company = request.META['HTTP_COMPANY']
        expense = Expense.objects.all()
        serializer = Expenseserializers(expense, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Expenseserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Expense.objects.get(id=id)
        except Expense.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Expense = self.get_object(id)
        serializer = Expenseserializers(Expense)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Expense = self.get_object(id)
        serializer = Expenseserializers(Expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Expense = self.get_object(id)
        Expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
