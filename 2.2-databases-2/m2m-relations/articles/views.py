from django.shortcuts import render
from articles.models import Article, ArticleScope, Tag
from django.db.models.query import Prefetch


def articles_list(request):
    template = 'articles/news.html'
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering).prefetch_related(
        Prefetch('scopes', ArticleScope.objects.order_by('-is_main', 'tag__name')))
    context = {'object_list': articles}

    return render(request, template, context)
