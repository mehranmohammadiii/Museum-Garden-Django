from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Memory
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MemoryForm,ImageFormSet



class MemoryCreate(LoginRequiredMixin,CreateView):
    model = Memory
    form = MemoryForm
    fields = ('title','text')
    template_name = 'memories/create_memory.html'
    context_object_name = 'memory'
    def get_success_url(self):
        return reverse('memories:memorylist')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST :
            data['image_formset'] = ImageFormSet(self.request.POST,self.request.FILES)
        else :
            data['image_formset'] =ImageFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context['image_formset']
        if form.is_valid() and image_formset.is_valid() :
            memory_instance = form.save(commit=False)
            memory_instance.user_register = self.request.user
            memory_instance.save()
            image_formset.instance = memory_instance
            image_formset.save()
            return super().form_valid(form)
        else :
            return self.render_to_response(self.get_context_data(form=form))



class MemoryList(LoginRequiredMixin,ListView):
    model = Memory
    template_name = 'memories/memory_list.html'
    context_object_name = 'memories'
    queryset = Memory.objects.filter(is_active = True).select_related('user_register').order_by('-register_date')