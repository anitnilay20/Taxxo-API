from product.models import Product
from product.serializers import Productserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        company = request.META['HTTP_COMPANY']
        product = Product.objects.filter(company_id=company)
        serializer = Productserializers(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Productserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        product = self.get_object(id)
        serializer = Productserializers(product)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        product = self.get_object(id)
        serializer = Productserializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
