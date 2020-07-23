from django.urls import path
from .views import SignUp, SignIn, SignIn_when_email_exists


urlpatterns = [
    path('/SignUp', SignUp.as_view()),
    path('/SignIn', SignIn.as_view()),
    path('/SignInStart', SignIn_when_email_exists.as_view())
]
