from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from geographic_services.provider.views import ProviderView

router = DefaultRouter(trailing_slash=False)
router.register(r'providers', ProviderView, basename='provider')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'docs/',
        SpectacularSwaggerView.as_view(
            template_name='swagger-ui.html', url_name='schema'
        ),
        name='swagger-ui',
    ),
]
