from rest_framework.response import Response
from rest_framework.views import APIView, status


class IndexView(APIView):
    def get(self, request):
        return Response({'success': True, "message": "Hello from the server!",}, status=status.HTTP_200_OK)