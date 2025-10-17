from django.shortcuts import render,get_object_or_404
from .models import Article,ArticleGallery
from django.core.paginator import Paginator
from django.db.models import F
# Create your views here.


def show_article(request):

    articles = Article.objects.filter(is_active=True).select_related('articletype').prefetch_related("author").order_by("-publication_date")
    paginator = Paginator(articles,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,"article/article_list.html",{"page_obj" : page_obj})


def show_article_detail(request,slug):
    article = get_object_or_404(Article,slug=slug,is_active=True)
    # request.session['last_viewed_article'] = {
    #     'slug': article.slug,
    #     'title': article.subject
    # }
    
    Article.objects.filter(slug=slug).update(view_number = F('view_number')+1)
    gallery_images = ArticleGallery.objects.filter(article=article)
    return render(request,"article/article_detail.html",{"article" : article, "gallery_images" : gallery_images})
    # response = render(request,"article/article_detail.html",{"article" : article, "gallery_images" : gallery_images})
    # response.set_cookie('last_viewed_slug', article.slug, max_age=30 * 24 * 60 * 60)
    # return response

