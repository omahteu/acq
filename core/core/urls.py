from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers
from django.contrib import admin
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Acqualog",
      default_version='v1',
      description="Este documento descreve os recursos disponíveis nesta API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@seusite.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()

urlpatterns = [
   path('admin/', admin.site.urls),
   path(r'api/', include((router.urls, 'api'), namespace='api')),
   path('api/autenticacao/', include(('apps.autenticacao.urls', 'core.apps.autenticacao'), namespace='autenticacao')),
   path('api/cliente/', include(('apps.clientes.urls', 'core.apps.clientes'), namespace='cliente')),
   path('api/fisico_quimicos/', include(('apps.fisico_quimicos.urls', 'core.apps.fisico_quimicos'), namespace='fisico_quimicos')),
   path('api/hidricos/', include(('apps.hidricos.urls', 'core.apps.hidricos'), namespace='hidricos')),
   path('api/hidrometricos/', include(('apps.hidrometricos.urls', 'core.apps.hidrometricos'), namespace='hidrometricos')),
   path('api/localidades/', include(('apps.localidades.urls', 'core.apps.localidades'), namespace='localidades')),
   path('api/microbiologicos/', include(('apps.microbiologicos.urls', 'core.apps.microbiologicos'), namespace='microbiologicos')),
   path('api/usuario/', include(('apps.usuarios.urls', 'core.apps.usuarios'), namespace='usuario')),

   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
