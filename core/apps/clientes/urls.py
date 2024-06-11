from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'cliente', ClienteViewsets, basename='cliente')

urlpatterns = router.urls
