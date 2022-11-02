# from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', include('custom_auth.urls')),
    path('events/', include('events_api.urls')),
    path('rooms/', include('rooms_api.urls')),
    path('books/', include('books_api.urls')),
]
