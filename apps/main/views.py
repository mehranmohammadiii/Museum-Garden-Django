from django.shortcuts import render
from django.conf import settings
# Create your views here.

def media_admin(request):
        return { "media_url" : settings.MEDIA_URL}
        



def index(request):
    context = {
        "media_url" : settings.MEDIA_URL
    }
    return render(request,'main/index.html')




# from apps.article.models import Article # <-- مدل Article را وارد می‌کنیم

# def index(request):
#     # ۱. slug آخرین مقاله بازدید شده را از کوکی می‌خوانیم
#     last_slug = request.COOKIES.get('last_viewed_slug')
#     last_article = None # یک متغیر خالی برای آن در نظر می‌گیریم

#     # ۲. اگر slug در کوکی وجود داشت...
#     if last_slug:
#         # ۳. ...مقاله مربوطه را از دیتابیس پیدا می‌کنیم
#         # .first() برای این است که اگر به هر دلیلی چند نتیجه پیدا شد، فقط اولی را برگرداند و خطا ندهد.
#         last_article = Article.objects.filter(slug=last_slug, is_active=True).first()
        
#     # ۴. متغیر last_article (که یا حاوی شیء مقاله است یا None) را به context اضافه می‌کنیم
#     context = {
#         "media_url" : settings.MEDIA_URL,
#         'last_article_viewed': last_article
#     }
    
#     # ۵. context را به قالب ارسال می‌کنیم
#     return render(request, 'main/index.html', context)