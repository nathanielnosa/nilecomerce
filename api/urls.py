from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/stores/',include('stores.urls')),
    path('api/users/',include('users.urls')),
    # jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
