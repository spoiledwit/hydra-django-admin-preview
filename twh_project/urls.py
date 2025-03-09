from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.views import PasswordResetConfirmView
from accounts.views import CustomPasswordResetConfirmView

admin.site.site_header = "Travel with Hydra"
admin.site.site_title = "Travel with Hydra"
admin.site.index_title = "Welcome to Travel with Hydra"


schema_view = get_schema_view(
   openapi.Info(
      title="Travel with Hydra API",
      default_version='v1',
      description="API documentation forTravel with Hydra APIs",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourproject.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cms/', include('cms.urls')),
    path('api/visa/', include('visa.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/password/reset/confirm/<uid>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/auth/reset-password-confirm/', CustomPasswordResetConfirmView.as_view(), name='reset-password-confirm'),
    path('accounts/', include('allauth.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path("ckeditor5/", include('django_ckeditor_5.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
