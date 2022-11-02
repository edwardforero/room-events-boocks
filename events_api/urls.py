from django.urls import include, path

from rest_framework import routers

from events_api.views import EventsView

router = routers.DefaultRouter()
router.register(r'', EventsView)

urlpatterns = router.urls