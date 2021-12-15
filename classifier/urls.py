from django.urls import path
from .views import ClassifierAPIView


urlpatterns = [
    path('classify', ClassifierAPIView.as_view()),
]
