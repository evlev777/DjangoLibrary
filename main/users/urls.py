from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import UserLoginView, UserRegistrationView, ProfileUserView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', login_required(ProfileUserView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout')
]