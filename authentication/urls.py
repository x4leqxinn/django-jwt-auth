from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import TaskViewSet

router: ExtendedSimpleRouter = ExtendedSimpleRouter()

router = routers.DefaultRouter()
router.register(r'task',TaskViewSet)

urlpatterns = [
    path('schema/',SpectacularAPIView.as_view(api_version="v1"),name='schema'),
    path('schema/swagger/',SpectacularSwaggerView.as_view(url_name='api:schema'),name='swagger'),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
    path('token/verify',TokenVerifyView.as_view(),name='token_verify'),
    path('',include(router.urls)),
]
