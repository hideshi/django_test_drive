from django.contrib.auth.models import Article, Help, TermsOfService
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-date_joined')
    serializer_class = ArticleSerializer

class HelpViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows help to be viewed or edited.
    """
    queryset = Help.objects.all().order_by('-date_joined')
    serializer_class = HelpSerializer

class TermsOfServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows terms of service to be viewed or edited.
    """
    queryset = TermsOfService.objects.all().order_by('-date_joined')
    serializer_class = TermsOfServiceSerializer

