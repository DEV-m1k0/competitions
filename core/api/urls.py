from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    # Генерация OpenAPI схемы
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
