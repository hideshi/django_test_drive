from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField

class Article(models.Model):
    def image_tag(self):
        return mark_safe('<img src="/media/{}" width="150" height="70" />'.format(self.image))

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='article/', default='article/default.png')
    image_tag.short_description = 'Image'
    content = HTMLField()
    author = models.ForeignKey(User)
    status_draft = 'draft'
    status_public = 'public'
    statuses = (
        (status_draft, 'Draft'),
        (status_public, 'Public'),
    )
    status = models.CharField(choices=statuses, default=status_draft, max_length=8)
    open_date = models.DateTimeField(blank=True, null=True)
    yes = 'yes'
    no = 'no'
    yes_no = (
        (yes, 'Yes'),
        (no, 'No'),
    )
    notify = models.CharField(choices=yes_no, default=yes, max_length=8)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Notification(models.Model):
    title = models.CharField(max_length=60)
    message = models.CharField(max_length=255)
    status = models.CharField(default='not_sent', max_length=10, editable=False)
    open_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Help(models.Model):
    description_ios = HTMLField()
    description_android = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class TermsOfService(models.Model):
    description_ios = HTMLField()
    description_android = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
