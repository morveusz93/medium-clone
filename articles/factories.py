from factory import Sequence, SubFactory, fuzzy, post_generation
from factory.django import DjangoModelFactory

from articles.models import Article, Author, Tag


class AuthorFactory(DjangoModelFactory):
    first_name = "Adam"
    last_name = Sequence(lambda n: 'Mickiewicz {0}'.format(n))

    class Meta:
        model = Author


class TagFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText()

    class Meta:
        model = Tag


class ArticleFactory(DjangoModelFactory):
    title = Sequence(lambda n: 'Article title {0}'.format(n))
    content = fuzzy.FuzzyText(length=120)
    author = SubFactory(AuthorFactory)

    class Meta:
        model = Article
