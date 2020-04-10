from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api_basic.views.functionviews import article_list, article_detail
from .views import classviews, mixinviews, genericviews
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView)

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

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
