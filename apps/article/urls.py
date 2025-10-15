from django.urls import path
from .views import show_article,show_article_detail
# from .views import index

app_name = 'article'
urlpatterns = [
    path('',show_article,name='blog'),
    path('<slug:slug>/',show_article_detail,name="detail")

]