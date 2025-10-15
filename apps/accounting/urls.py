from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'accounting'

urlpatterns = [
        path('signup/',SignUpView.as_view(),name='signup'),
        path('login/',LoginView.as_view(template_name='accounting/login.html'),name='login'),
        path('logout/',LogoutView.as_view(),name='logout')

]