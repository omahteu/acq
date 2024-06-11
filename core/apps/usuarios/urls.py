from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'perfil', PerfilView, basename='perfil')
router.register(r'', UsuariosView, basename='usuarios')

urlpatterns = router.urls
