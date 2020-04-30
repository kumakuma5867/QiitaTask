from rest_framework import routers
from tasks.views import TaskViewSet


router = routers.SimpleRouter()
router.register('', TaskViewSet)

urlpatterns = router.urls
