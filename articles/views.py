from django.views.generic import DetailView

from articles.models import Article


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
