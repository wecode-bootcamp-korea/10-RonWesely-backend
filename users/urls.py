from django.urls import path

from .views import (
    SignUp,
    SignIn,
    SignInWhenEmailExists,
    MyPage
)

urlpatterns = [
    path('/SignUp', SignUp.as_view()),
    path('/SignIn', SignIn.as_view()),
    path('/SignInStart', SignInWhenEmailExists.as_view()),
    path('/MyPage',  MyPage.as_view())
]
