from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import UserLoginView, UserRegistrationView, ProfileUserView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', login_required(ProfileUserView.as_view()), name='profile'),
]