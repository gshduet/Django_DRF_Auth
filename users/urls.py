from django.urls import path

from .views import SignUpView, DjangoSignInView, LogoutView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/logout', LogoutView.as_view()),
    path('/auth/django', DjangoSignInView.as_view())
]