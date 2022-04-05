from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from django.views import generic
from account.models import Profile
from main.utils import *

from .forms import *

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


# EDIT USER`S PROFILE

class UserEditView(generic.UpdateView):
    form_class = EditUserForm
    template_name = 'account/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


# USER CHANGE PASSWORD PAGE

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

# PASSWORD SUCCESS CHANGED PAGE


def password_success(request):
    return render(request, 'account/password_success.html', {})


# EDIT USER IMAGE

class EditUserImage(generic.UpdateView):
    model = Profile
    fields = ['profile_pic', ]
    template_name = 'account/edit_profile_image.html'
    success_url = reverse_lazy('home')


# SHOW USER PAGE

class ShowUserPageView(DetailView):
    model = Profile
    template_name = 'account/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowUserPageView, self).get_context_data(
            *args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
