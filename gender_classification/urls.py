from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import IndexView

schema_view = get_schema_view(
        openapi.Info(
            title="Unrepy Gender Classification API",
            default_version='v1',
            description="Testing",
            terms_of_service="https://www.unreply.herokuapp.com/policies/terms/",
            contact=openapi.Contact(email="contact@unreply.com"),
            license=openapi.License(name="MIT License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/', include('classifier.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)