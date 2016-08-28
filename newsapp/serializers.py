from django.contrib.auth.models import User
from .models import Article, Category, Help, TermsOfService
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'author_id', 'category_id', 'status', 'open_date', 'created', 'modified')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class HelpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Help
        fields = ('description_ios', 'description_android')

class TermsOfServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TermsOfService
        fields = ('description_ios', 'description_android')
