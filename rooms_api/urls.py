from rest_framework import routers

from rooms_api.views import RoomsView

router = routers.DefaultRouter()
router.register(r'', RoomsView)

urlpatterns = router.urls