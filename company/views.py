from company.models import Company
from company.serializers import Companyserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CompanytList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        admin = request.META['HTTP_ADMIN']
        company = Company.objects.filter(admin=admin)
        serializer = Companyserializers(company, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Companyserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CompanyDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Company = self.get_object(id)
        serializer = Companyserializers(Company)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Company = self.get_object(id)
        serializer = Companyserializers(Company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Company = self.get_object(id)
        Company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
