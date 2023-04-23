from django.urls import path, include

urlpatterns = [
    path('documentation/', include(('api.v1.base.urls','api-base'),namespace='api-base')),
    path('task/', include(('api.v1.task.urls', 'api-tasks'), namespace='api-tasks')),
    path('auth/', include(('api.v1.authentication.urls','api-auth'),namespace='api-auth')),
]
