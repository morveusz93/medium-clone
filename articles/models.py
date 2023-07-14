from django.db import models
from authors.models import Author


class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - by {self.author}"

    class Meta:
        ordering = ['-pub_date']
