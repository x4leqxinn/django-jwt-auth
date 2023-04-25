from django.urls import path, include

urlpatterns = [
    path('docs/', include(('api.v1.base.urls','api-base'),namespace='api-base')),
    path('auth/', include(('api.v1.authentication.urls','api-auth'),namespace='api-auth')),
]
