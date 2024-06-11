from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'localidade', LocalidadeViewsets, basename='localidade')

urlpatterns = router.urls
