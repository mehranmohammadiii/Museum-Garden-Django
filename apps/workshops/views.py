from django.shortcuts import render
from django.db.models import F
from .models import Workshop
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


app_name = 'workshop'

class WorkshopListView(ListView):
    model = Workshop
    template_name = 'workshop/workshop_list.html'
    context_object_name = 'workshops'
    paginate_by = 2
# --------------------------------------------------
class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'workshop/workshop_detail.html'
    context_object_name = 'workshop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['gallery_images'] = self.object.gallery_images.all()
        return context
    
    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        Workshop.objects.filter(pk=obj.pk).update(view_number =F('view_number')+1 )
        return obj