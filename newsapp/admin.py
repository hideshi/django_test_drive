from django.contrib import admin
from .models import Article, Notification, Help, TermsOfService

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    def get_queryset(self, request): 
        qs = super(ArticleAdmin, self).get_queryset(request) 
        if request.user.username == 'admin':
            return qs
        else:
            return qs.filter(author=request.user)

    search_fields = ['title', 'content']
    list_display = ('title', 'image_tag', 'status', 'open_date')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    search_fields = ['title', 'message']
    list_display = ('title', 'status', 'open_date')

@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

@admin.register(TermsOfService)
class TermsOfServiceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True
