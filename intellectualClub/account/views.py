from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from main.utils import *

from .forms import *


def edit_profile(request):
    return render(request, 'account/edit_profile.html')

    #  REGISTER USER CLASS


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация пользователей')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


# LOGIN USER CLASS

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'account/login.html'

    def get_context_data(self, *, object_list=None, **kwarg):
        context = super().get_context_data(**kwarg)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

# LOGOUT USER


def logout_user(request):
    logout(request)
    return redirect('login')


# USER ACCOUNT
class UserAccount(LoginRequiredMixin, DataMixin, TemplateView):
    model = User
    template_name = 'account/account.html'
    raise_exception = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Мой аккаунт')
        return dict(list(context.items()) + list(c_def.items()))


# USER SETTINGS FORM
# def user_settings(request):
#     if request.method == 'POST':
#         form = UserSettingsForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.update()
#                 return redirect('account')
#             except:
#                 form.add_error(None, 'Ошибка изменения данных')
#     else:
#         form = UserSettingsForm()
#     return render(request, 'main/account.html', {'form': form})
