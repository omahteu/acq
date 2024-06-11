from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"hidrometrico", HidrometricoViewSets, basename="hidrometrico")

urlpatterns = router.urls
