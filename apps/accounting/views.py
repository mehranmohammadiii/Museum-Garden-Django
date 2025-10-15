from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import View
# from django.contrib import messages
# from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login


# --------------------------------------------------------------
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('main:index')
    template_name = 'accounting/signup.html'

    def form_valid(self, form):
        response =  super().form_valid(form)
        user = form.save()
        login(self.request,user)
        return response
# --------------------------------------------------------------

    