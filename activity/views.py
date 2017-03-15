from activity.models import Activity
from activity.serializers import Activityserializers
from rest_framework.views import APIView
from rest_framework.response import Response


class ActivtyList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        company = request.META['HTTP_COMPANY']
        activity = Activity.objects.filter(company_id=company).order_by('-date')
        serializer = Activityserializers(activity, many=True)
        return Response(serializer.data)
