from django.shortcuts import render,get_object_or_404
from .models import Article,ArticleGallery,ArticleLike
from django.core.paginator import Paginator
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from django.contrib.auth.mixins import LoginRequiredMixin

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


# @login_required
# def like_article_view(request,pk):
#     if request.method=='POST':
#         try:
#             article=Article.objects.get(id=pk)
#             article.likes+=1
#             article.save()
#             return JsonResponse({'status':'ok','likes_count':article.likes})
#         except Article.DoesNotExist:
#             return JsonResponse({'status':'error','message':'Article not found0'},status = 404)

#     return JsonResponse({'status':'erroe','message':'invalid not found'},status = 400)


@login_required
def like_article_view(request,pk):
    if request.method=='POST':
      article = get_object_or_404(Article,id=pk)  
      like, status =  ArticleLike.objects.get_or_create(user=request.user,article=article) 
      if status :
          article.likes=F('likes')+1
          article.save()
          article.refresh_from_db()
          return JsonResponse({'status': 'ok', 'message': 'liked', 'likes_count': article.likes})
      else:
          return JsonResponse({'status': 'error', 'message': 'already_liked', 'likes_count': article.likes})
