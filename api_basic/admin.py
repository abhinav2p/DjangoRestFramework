from django.contrib import admin

from .forms import *
from .models import *


class ArticleForm(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'email']
    form = ArticleApiForm


class SnippetForm(admin.ModelAdmin):
    list_display = ['id', 'created', 'title', 'linenos', 'language', 'style']
    form = SnippetApiForm


admin.site.register(Article, ArticleForm)
admin.site.register(Snippet, SnippetForm)
