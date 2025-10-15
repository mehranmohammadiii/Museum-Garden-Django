from django.shortcuts import render,redirect
from .models import Locations,Ticket,Contact
from .forms import MessageForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseNotFound
from django.contrib import messages
# Create your views here.

def show_histori(request):
    return render(request,'locations/histori.html')
# ---------------------------------------------------------------------------------------------
def show_parts(request):
    locations =Locations.objects.all()
    return render(request,'locations/locations.html',{"locations": locations})
# ---------------------------------------------------------------------------------------------
def show_part(request,id):
    location =Locations.objects.get(id=id)
    return render(request,'locations/location.html',{"location": location})
# ---------------------------------------------------------------------------------------------
def show_visitor_guide(request):
    tickets = Ticket.objects.select_related('visitortype','location').all()
    return render(request,'locations/visitor_guide.html',{"tickets":tickets})
# ---------------------------------------------------------------------------------------------
# def download_path_pdf(request):
#     fs = FileSystemStorage()
#     file_name = 'pdf_file/location.pdf'
#     if fs.exists(file_name):
#         with fs.open(file_name) as pdf :
#             response=HttpResponse(pdf,content_type='application/pdf' )
#             response['content-disposition'] =" attachment; filename=location.pdf"
#             return response
#     else :
#         return HttpResponseNotFound("فایل بیدا نشد")

# ---------------------------------------------------------------------------------------------
def show_contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"  پیام شما با موفقیت ارسال شد.سپاس گزاریم")
            return redirect('locations:contact') 
    else:
        form = MessageForm()
    return render(request, "locations/contact.html", {"form": form})

# def show_contact(request):
#     form = MessageForm(request.POST)
#     if form.is_valid():
#         form_clean = form.cleaned_data
#         contact = Contact()
#         contact.full_name = form_clean["full_name"]
#         contact.email = form_clean["email"]
#         contact.subject = form_clean["subject"]
#         contact.message = form_clean["message"]
#         contact.save()
#         return redirect("main:index")
#     return render(request,"locations/contact.html",{"form":form})
# ---------------------------------------------------------------------------------------------


