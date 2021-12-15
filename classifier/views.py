from rest_framework import generics, serializers, views, status
from rest_framework.response import Response


class ClassifierAPIView(generics.GenericAPIView):
    
    def get(self, request):
        return Response({'success': True}, status=status.HTTP_200_OK)