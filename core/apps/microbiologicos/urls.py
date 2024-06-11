from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'microbiologico', MicrobiologicoViewsets, basename='microbiologico')

urlpatterns = router.urls
