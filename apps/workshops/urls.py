from django.urls import path
from .views import WorkshopListView,WorkshopDetailView
# from .views import index

app_name = 'workshop'
urlpatterns = [
    path('',WorkshopListView.as_view(),name='workshoplistview'),
    path('<int:pk>/',WorkshopDetailView.as_view(),name='workshopdetailview'),

]