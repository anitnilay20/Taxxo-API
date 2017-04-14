from journal.models import Journal
from journal.serializers import Journalserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class JournalList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        company = request.META['HTTP_COMPANY']
        journal = Journal.objects.filter(company_id=company)
        serializer = Journalserializers(journal, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Journalserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JournalDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Journal.objects.get(id=id)
        except Journal.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Journal = self.get_object(id)
        serializer = Journalserializers(Journal)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Journal = self.get_object(id)
        serializer = Journalserializers(Journal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Journal = self.get_object(id)
        Journal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
