from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from articles.forms import CommentForm
from articles.models import Article


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    form_class = CommentForm
    context_object_name = 'article'

    def get_success_url(self):
        return reverse('article-details', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'article': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ArticleDetailView, self).form_valid(form)
