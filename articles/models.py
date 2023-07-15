from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=64)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} - by {self.author}"

    class Meta:
        ordering = ['-pub_date']


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
