from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('schema/',SpectacularAPIView.as_view(api_version="v1"),name='schema'),
    path('schema/swagger/',SpectacularSwaggerView.as_view(url_name='api-v1:api-base:schema'),name='swagger'),
]
