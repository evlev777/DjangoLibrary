from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .models import User


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    title = 'Library - Авторизация'


    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request=request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('library:index')
        else:
            return render(
                request=request,
                template_name=self.template_name,
                context={'form': form}
            )


class UserRegistrationView(CreateView, SuccessMessageMixin):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрированы'
    title = 'Library - Регистрация'

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрированы')
            return redirect('users:login')
        else:
            return render(
                request=request,
                template_name=self.template_name,
                context={'form': form}
            )


class ProfileUserView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

