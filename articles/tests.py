from django.test import TestCase
from django.urls import reverse

from articles.factories import ArticleFactory, TagFactory


class TestArticleListView(TestCase):
    def setUp(self):
        self.articles = []
        self.url = reverse('article-list')

    def test_article_at_list_view(self):
        self.create_articles()
        response = self.client.get(self.url)
        response_article_list = list(response.context_data["article_list"])

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Article list')
        self.assertEquals(len(response_article_list), len(self.articles))
        self.assertListEqual(self.articles, response_article_list)

    def test_paginate_by_5(self):
        paginate_by = 5
        self.create_articles(num=paginate_by + 1)
        response = self.client.get(self.url)
        response_article_list = list(response.context_data["article_list"])

        self.assertEquals(len(response_article_list), paginate_by)
        self.assertTrue(response.context_data["is_paginated"])
        self.assertNotIn(self.articles[0], response_article_list)

    def create_articles(self, num: int = 1, **kwargs):
        for _ in range(num):
            article = ArticleFactory.build(**kwargs)
            article.author.save()
            article.save()
            self.articles.append(article)


class TestArticleDetailView(TestCase):
    def setUp(self):
        self.article = ArticleFactory.build()
        self.article.author.save()
        self.article.save()
        self.url = reverse('article-detail', kwargs={'pk': self.article.pk})

    def test_article_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.article.title)
        self.assertContains(response, self.article.content)

    def test_article_in_context(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['article'], self.article)


class TagListViewTest(TestCase):
    def setUp(self):
        self.url = reverse('tag-list')
        self.tags = []

    def test_tag_list_view(self):
        self.create_tags()
        response = self.client.get(self.url)
        response_tag_list = list(response.context_data["tag_list"])

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tag list')
        self.assertEquals(len(response_tag_list), len(self.tags))
        self.assertListEqual(self.tags, response_tag_list)

    def test_paginate_by_5(self):
        paginate_by = 5
        self.create_tags(num=paginate_by + 1)
        response = self.client.get(self.url)
        response_tag_list = list(response.context_data["tag_list"])

        self.assertEquals(len(response_tag_list), paginate_by)
        self.assertTrue(response.context_data["is_paginated"])
        self.assertNotIn(self.tags[0], response_tag_list)

    def create_tags(self, num: int = 1, **kwargs):
        for _ in range(num):
            tag = TagFactory.build(**kwargs)
            tag.save()
            self.tags.append(tag)


class TagDetailViewTest(TestCase):
    def setUp(self):
        self.tag = TagFactory.build()
        self.tag.save()
        self.article = ArticleFactory.build()
        self.article.author.save()
        self.article.save()
        self.article.tags.add(self.tag)
        self.article.save()
        self.url = reverse('tag-detail', kwargs={'pk': self.tag.pk})

    def test_tag_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tag.name)
        self.assertContains(response, self.article.title)

    def test_tag_detail_context(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['tag'], self.tag)
        self.assertEqual(list(response.context['object_list']), [self.article])