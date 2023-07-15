from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from articles.models import Article, Author, Tag


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Tag)
