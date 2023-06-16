from django.urls import path, include


urlpatterns = [
    path('docs/', include(('api.v1.base.urls', 'api-v1:api-base'), namespace='api-base')),
    path('auth/', include(('api.v1.authentication.urls', 'api-v1:api-auth'), namespace='api-auth')),
]