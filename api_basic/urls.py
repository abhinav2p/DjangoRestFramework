from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api_basic.views.functionviews import article_list, article_detail
from .views import classviews, mixinviews, genericviews

urlpatterns = [
    path('articles/', article_list),
    path('', article_list),
    path('article/<int:pk>/', article_detail),
    path('clarticles/', classviews.ArticleList.as_view()),
    path('clarticle/<int:pk>/', classviews.ArticleDetail.as_view()),
    path('mxarticles/', mixinviews.ArticleMixinList.as_view()),
    path('mxarticle/<int:pk>/', mixinviews.ArticleMixinDetail.as_view()),
    path('garticles/', genericviews.GenericArticleList.as_view()),
    path('garticle/<int:pk>/', genericviews.GenericArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
