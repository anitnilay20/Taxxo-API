from contra.models import Contra
from contra.serializers import Contraserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ContraList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self,request, format=None):
        company =request.META['HTTP_COMPANY']
        contra = Contra.objects.all()
        serializer = Contraserializers(contra, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Contraserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContraDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Contra.objects.get(id=id)
        except Contra.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Contra = self.get_object(id)
        serializer = Contraserializers(Contra)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Contra = self.get_object(id)
        serializer = Contraserializers(Contra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Contra = self.get_object(id)
        Contra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
