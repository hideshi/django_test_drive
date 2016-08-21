from django.contrib.auth.models import Article, Help, TermsOfService
from rest_framework import serializers

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'author', 'status', 'open_date')

class HelpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Help
        fields = ('description')

class TermsOfServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TermsOfService
        fields = ('description')
