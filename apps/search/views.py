from django.shortcuts import render
from django.db.models import Q
from apps.article.models import Article
from apps.workshops.models import Workshop



def search_view(request):
    query = request.GET.get('q')
    articles = []
    workshops = []
    if query :
        article_query = Q(subject__icontains=query) | Q(text__icontains=query)
        articles = Article.objects.filter(article_query, is_active=True).distinct()

        # workshop_query = Q(title__icontains=query) | Q(information__icontains=query)
        workshop_query = Q(title__icontains=query) | Q(information__icontains=query)
        workshops = Workshop.objects.filter(workshop_query, is_active=True).distinct()

    context = {
        'query': query,
        'articles': articles,
        'workshops': workshops,
    }
    return render(request, 'search/search_results.html', context)