from rest_framework import mixins, generics
from api_basic.models import Article
from api_basic.serializers import ArticleSerializer
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework import permissions

class ArticleMixinList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [permissions.AllowAny]


    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleMixinDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
