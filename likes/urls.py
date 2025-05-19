from rest_framework.routers import DefaultRouter
from .views import LikeViewSet

router = DefaultRouter()
router.register(r'like', LikeViewSet)

urlpatterns = router.urls
