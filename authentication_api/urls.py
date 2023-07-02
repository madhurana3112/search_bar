from django.urls import path
from .views import SignupAPI, SigninAPI, VerifyOTPAPI, LogoutAPI

urlpatterns = [
    path('signup/', SignupAPI.as_view(), name='api-signup'),
    path('signin/', SigninAPI.as_view(), name='api-signin'),
    path('verify-otp/', VerifyOTPAPI.as_view(), name='api-verify-otp'),
    path('logout/', LogoutAPI.as_view(), name='api-logout'),
]
