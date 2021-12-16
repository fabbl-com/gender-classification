from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
    
def IndexView(request):
    return JsonResponse({'success': True, 'message': 'hello from server!'})

urlpatterns = [
    path('', IndexView),
    path('admin/', admin.site.urls),
    path('api/v1/', include('classifier.urls'))
]