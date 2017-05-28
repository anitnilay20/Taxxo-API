from Customer.models import Profile
from Customer.serializers import UserSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Taxxo.settings import AUTH_USER_MODEL


class CustomerList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, format=None):
        customer = Profile.objects.all()
        serializer = UserSerializers(customer, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        profile = self.get_object(id)
        serializer = UserSerializers(profile)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        profile = self.get_object(id)
        serializer = UserSerializers(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        profile = self.get_object(id)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerLogin(APIView):
    def post(self, request, format=None):
        email = request.data['email']
        password = request.data['password']
        try:
            customer = Profile.objects.get(email=email, password=password)
            serializer = UserSerializers(customer, many=False)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
