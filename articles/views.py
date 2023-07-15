from django.views.generic import DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articles.models import Article, Tag


class ArticleListView(ListView):
    model = Article
    context_object_name = "article_list"
    paginate_by = 5


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"


class TagListView(ListView):
    model = Tag
    context_object_name = "tag_list"
    paginate_by = 5


class TagDetailView(DetailView, MultipleObjectMixin):
    model = Tag
    context_object_name = "tag"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(tags=self.object).all()
        context = super(TagDetailView, self).get_context_data(
            object_list=object_list, **kwargs
        )
        return context
