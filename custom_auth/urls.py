from django.urls import include, path

from rest_framework import routers

from custom_auth.views import CustomUserView

router = routers.DefaultRouter()
router.register(r'', CustomUserView)

urlpatterns = [
   path('', include(router.urls)),
]