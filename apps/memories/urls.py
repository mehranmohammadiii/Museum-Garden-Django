from django.urls import path
from .views import MemoryCreate,MemoryList

app_name = 'memories'

urlpatterns = [
        path('',MemoryList.as_view(),name='memorylist'),
        path('add/',MemoryCreate.as_view(),name='memorycreate'),

]