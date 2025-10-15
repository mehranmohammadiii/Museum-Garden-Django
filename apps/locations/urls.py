from django.urls import path
from .views import show_histori,show_parts,show_part,show_visitor_guide,show_contact
# from .views import index

app_name = 'locations'
urlpatterns = [
    path('hostori/',show_histori,name='histori'),
    path('parts/',show_parts,name='parts'),
    path('part/<int:id>/',show_part,name='part'),
    path('guide/',show_visitor_guide,name='visitor_guide'),
    path('contact/',show_contact,name='contact'),
    # path('pdf_path/',download_path_pdf,name='pdf_path')
]
