import random

from django.core.management.base import BaseCommand
from django.db import IntegrityError

from articles.models import *


class Command(BaseCommand):
    help = "Populate DB with fake data"

    def handle(self, *args, **options):
        authors = self.create_authors()
        tags = self.create_tags()
        self.create_articles(authors, tags)

        self.stdout.write(self.style.SUCCESS("Database successfully populated!"))

    def create_authors(self):
        authors = []
        for i in range(20):
            author = Author(first_name="The", last_name="Author" + str(i))
            author.save()
            authors.append(author)
        return authors

    def create_tags(self):
        tag_names = [
            "Recipies",
            "Tech",
            "Movies",
            "Sport",
            "Music",
            "Animals",
            "Culture",
        ]
        tags = []
        for i in tag_names:
            tag = Tag(name=i)
            try:
                tag.save()
            except IntegrityError:
                continue
            tags.append(tag)
        if not tags:
            tags = Tag.objects.all()
        return tags

    def create_articles(self, authors, tags):
        lorem = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nec orci vulputate, gravida mi "
            "pretium, consectetur lorem. Proin a orci a dui tristique viverra quis sed metus. Nam a augue non "
            "nibh hendrerit pulvinar. Proin sit amet ultricies justo, at ullamcorper augue. Sed imperdiet, "
            "turpis ut scelerisque tincidunt, arcu orci aliquet felis, id vehicula augue diam non ipsum. "
            "Curabitur et placerat tellus. In quis fermentum purus. Donec scelerisque viverra tincidunt. "
            "Pellentesque sed neque nibh. Integer arcu tortor, laoreet nec interdum nec, feugiat nec leo. "
            "Maecenas interdum enim volutpat purus iaculis pellentesque. In in ullamcorper turpis, at viverra "
            "justo. Nunc convallis turpis sed ipsum scelerisque, non eleifend odio lacinia. Maecenas quis elit "
            "quam. Aenean tristique sodales dolor, egestas maximus risus viverra bibendum. Aliquam sit amet "
            "aliquam sapien. Vestibulum magna neque, commodo sed dictum non, varius ut orci. Donec at elit ut "
            "enim dapibus consequat nec ut mi. Donec sodales mauris ut fermentum faucibus. Nunc ut eros at mi "
            "luctus dictum eu eu felis. Duis feugiat urna a vehicula aliquam. Sed sed est iaculis, molestie quam "
            "at, posuere velit. Sed congue mauris lorem, et hendrerit diam sollicitudin non. Etiam laoreet eu "
            "mauris nec eleifend. Pellentesque vel tincidunt nibh, vel consequat nibh. Curabitur vehicula massa "
            "libero, vel varius dolor accumsan in. Nam nulla magna, mollis ut eros in, ornare sollicitudin "
            "sapien. Aenean sed efficitur tortor. Aenean in sem augue. Cras pulvinar magna commodo, rutrum erat "
            "at, facilisis nulla. Morbi malesuada semper magna, sed bibendum nisi interdum vel. Ut eget sagittis "
            "lacus, ut sodales tellus. Mauris accumsan fringilla ante eget convallis. Integer purus arcu, "
            "vehicula eu interdum a, tincidunt non mi. Nam commodo leo sit amet mollis suscipit. Nullam bibendum "
            "dui ac felis ultrices iaculis et ac mi. Fusce ut mauris quis arcu lacinia luctus non hendrerit orci. "
            "In consequat gravida enim. Nunc dui nulla, luctus vitae euismod quis, mollis id arcu. Curabitur "
            "elementum ipsum laoreet interdum aliquam. Praesent eu lacus in urna aliquet scelerisque. Cras non ex "
            "sed dolor rhoncus sagittis et quis neque. Nam sed orci cursus, fringilla turpis ac, volutpat mi. Nam "
            "quam libero, elementum quis dui ac, facilisis porttitor elit. Nullam semper turpis mauris, "
            "non pulvinar erat auctor non. Ut tristique, eros vel efficitur dictum, velit odio efficitur elit, "
            "sit amet luctus tellus tortor eget nisl. Quisque et leo et ligula scelerisque tincidunt. Sed posuere "
            "sem pharetra orci faucibus, id fringilla erat lacinia. Donec sollicitudin tellus sit amet turpis "
            "efficitur varius. Proin sit amet nulla sit amet massa consequat tempus et sagittis purus. Aliquam at "
            "tellus non urna lobortis feugiat vel at eros. Cras aliquet arcu dapibus est vestibulum, ac vehicula "
            "ex sollicitudin. Donec malesuada nunc velit, vitae varius quam euismod sed."
        )
        articles = []
        for i in range(100):
            article = Article(
                title="title " + str(i), author=random.choice(authors), content=lorem
            )
            article.save()
            article.tags.set(random.choices(tags, k=random.randint(1, len(tags))))
            article.save()
            articles.append(article)
