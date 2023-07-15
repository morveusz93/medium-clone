from django.views.generic import DetailView, ListView
from articles.models import Article


class ArticlesListView(ListView):
    model = Article
    context_object_name = 'articles_list'
    paginate_by = 5


class ArticleDetailView( DetailView):
    model = Article
    context_object_name = 'article'
