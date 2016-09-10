from rest_framework import routers
from .views import CategoryViewSet, ArticleViewSet, AuthorViewSet, HelpViewSet, TermsOfServiceViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('articles', ArticleViewSet)
router.register('authors', AuthorViewSet)
router.register('helps', HelpViewSet)
router.register('termsofservices', TermsOfServiceViewSet)
