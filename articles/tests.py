from django.test import RequestFactory, TestCase

from articles.factories import ArticleFactory
from articles.views import ArticleListView


class TestArticleListView(TestCase):
    def setUp(self):
        self.articles = []

    def test_article_at_list_view(self):
        self.create_articles()
        self.make_request()
        response_article_list = list(self.response.context_data["article_list"])

        self.assertEquals(len(response_article_list), len(self.articles))
        self.assertListEqual(self.articles, response_article_list)

    def test_paginate_by_5(self):
        paginate_by = 5
        self.create_articles(num=paginate_by + 1)
        self.make_request()
        response_article_list = list(self.response.context_data["article_list"])

        self.assertEquals(len(response_article_list), paginate_by)
        self.assertTrue(self.response.context_data["is_paginated"])
        self.assertNotIn(self.articles[0], response_article_list)

    def create_articles(self, num: int = 1, **kwargs):
        for _ in range(num):
            article = ArticleFactory.build(**kwargs)
            article.author.save()
            article.save()
            self.articles.append(article)

    def make_request(self):
        request = RequestFactory().get("/")
        view = ArticleListView()
        view.setup(request)
        self.response = view.get(request)
