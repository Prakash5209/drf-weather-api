from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',include('weather.urls',namespace="weather")),
    path('account/',include('account.urls',namespace="account")),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
