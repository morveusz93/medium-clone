from factory import Sequence, SubFactory, fuzzy, post_generation
from factory.django import DjangoModelFactory

from articles.models import Article, Author, Tag


class AuthorFactory(DjangoModelFactory):
    first_name = "Adam"
    last_name = Sequence(lambda n: f"Mickiewicz {n}")

    class Meta:
        model = Author


class TagFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText()

    class Meta:
        model = Tag


class ArticleFactory(DjangoModelFactory):
    title = Sequence(lambda n: f"Article title {n}")
    content = fuzzy.FuzzyText(length=120)
    author = SubFactory(AuthorFactory)

    class Meta:
        model = Article
