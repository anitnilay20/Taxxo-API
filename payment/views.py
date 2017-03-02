from payment.models import Payment
from payment.serializers import Paymentserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PaymentList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None, ):
        company = request.META['HTTP_Company']
        payment = Payment.objects.filter(company_id=company)
        serializer = Paymentserializers(payment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Paymentserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return Payment.objects.get(id=id)
        except Payment.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Payment = self.get_object(id)
        serializer = Paymentserializers(Payment)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Payment = self.get_object(id)
        serializer = Paymentserializers(Payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Payment = self.get_object(id)
        Payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
