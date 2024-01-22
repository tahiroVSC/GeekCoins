from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from apps.users.views import UserAPIViewsSet, UserRegisterAPI

router = DefaultRouter()
router.register('user', UserAPIViewsSet, 'api_users')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='api_users_login'),
    path('refresh/', TokenRefreshView.as_view(), name='api_users_refresh'),
    path('register/', UserRegisterAPI.as_view(), name="api_users_register"),
    
]

# from apps.users.views import CoinInfoAPIView

# router = DefaultRouter()

# router.register('coin', CoinInfoAPIView, basename='api_coin')

urlpatterns += router.urls