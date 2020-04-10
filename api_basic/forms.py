from django import forms

from .models import Article, Snippet


class ArticleApiForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class SnippetApiForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = '__all__'
