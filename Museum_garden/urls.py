"""
URL configuration for Museum_garden project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls',namespace='main'), name='main'),
    path('locations/', include('apps.locations.urls',namespace='locations'), name='locations'),
    path('blog/', include('apps.article.urls',namespace='article'), name='Article'),
    path('workshops/', include('apps.workshops.urls',namespace='workshop'), name='workshop'),
    path('accounts/', include('apps.accounting.urls',namespace='accounting'), name='account'),
    path('memories/', include('apps.memories.urls',namespace='memories'), name='memories'),
    path('search/', include('apps.search.urls',namespace='search'), name='search'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
