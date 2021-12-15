from django.urls import path
from .views import ClassifierAPIView

urlpatterns = [
    path('', ClassifierAPIView.as_view()),
]
