from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'fisico_quimico', FisicoQuimicoViewSets, basename='fisico_quimico')

urlpatterns = router.urls