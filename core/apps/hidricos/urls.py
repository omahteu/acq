from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'hidricos', HidricosViewsets, basename='hidricos')

urlpatterns = router.urls