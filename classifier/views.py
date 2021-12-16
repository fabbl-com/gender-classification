from rest_framework import generics, status
from rest_framework.response import Response
from classifier.serializers import ClassifierSerializer
from .ml.classify import classify
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

BASE_DIR = settings.BASE_DIR
class ClassifierAPIView(generics.CreateAPIView):
    serializer_class = ClassifierSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid(raise_exception=True):
            wav_file = request.FILES['audio']
            fs = FileSystemStorage()
            fs.save(wav_file.name, wav_file)
            abs_path = os.path.join(BASE_DIR, "uploads", wav_file.name)
            result = classify(abs_path)
            if os.path.exists(abs_path):
                os.remove(abs_path)
            return Response({'success': True, 'result': result}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
