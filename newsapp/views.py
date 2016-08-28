from django.contrib.auth.models import User
from .models import Category, Article, Help, TermsOfService
from .serializers import CategorySerializer, ArticleSerializer, AuthorSerializer, HelpSerializer, TermsOfServiceSerializer
from rest_framework import viewsets

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed.
    """
    queryset = Article.objects.all().order_by('-open_date')
    serializer_class = ArticleSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed.
    """
    queryset = User.objects.all()
    serializer_class = AuthorSerializer

class HelpViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows help to be viewed.
    """
    queryset = Help.objects.all()
    serializer_class = HelpSerializer

class TermsOfServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows terms of service to be viewed.
    """
    queryset = TermsOfService.objects.all()
    serializer_class = TermsOfServiceSerializer

