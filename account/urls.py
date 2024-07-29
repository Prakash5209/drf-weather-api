from django.urls import path

from account.views import UserRegistrationView,EmailVerification,ResetPasswordView

app_name = "account"
urlpatterns = [
    path('api/registration/',UserRegistrationView.as_view(),name='userRegistrationView'),
    path('api/email-verification/',EmailVerification.as_view(),name="emailVerification"),
    path('api/reset-password/',ResetPasswordView.as_view(),name="resetpasswordview")
]
