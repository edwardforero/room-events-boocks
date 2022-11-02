from rest_framework import routers

from books_api.views import BooksView

router = routers.DefaultRouter()
router.register(r'', BooksView)

urlpatterns = router.urls