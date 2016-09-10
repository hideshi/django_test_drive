from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    name = models.CharField(_('Name'), max_length=20)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified'), auto_now=True)

class Article(models.Model):
    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def image_tag(self):
        return mark_safe('<img src="/media/{}" width="150" height="70" />'.format(self.image))

    title = models.CharField(_('Title'), max_length=255)
    image = models.ImageField(_('Image'), null=True, upload_to='article/', default='article/default.png')
    image_tag.short_description = _('Image')
    content = RichTextUploadingField(verbose_name=_('Content'), null=True)
    author = models.ForeignKey(User, verbose_name=_('Author'))
    category = models.ForeignKey(Category, null=True, verbose_name=_('Category'))
    status_draft = 'draft'
    status_public = 'public'
    statuses = (
        (status_draft, _('Draft')),
        (status_public, _('Public')),
    )
    status = models.CharField(_('Status'), choices=statuses, default=status_draft, max_length=8)
    open_date = models.DateTimeField(_('Open date'), blank=True, null=True)
    yes = 'yes'
    no = 'no'
    yes_no = (
        (yes, _('Yes')),
        (no, _('No')),
    )
    notify = models.CharField(_('Notify'), choices=yes_no, default=yes, max_length=8)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified'), auto_now=True)

class Notification(models.Model):
    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')

    title = models.CharField(_('Title'), max_length=60)
    message = models.CharField(_('Message'), max_length=255)
    not_sent = 'Not sent'
    sent = 'Sent'
    sent_status = (
        (not_sent, _('Not sent')),
        (sent, _('Sent')),
    )
    status = models.CharField(_('Status'), choices=sent_status, default=not_sent, max_length=10, editable=False)
    open_date = models.DateTimeField(_('Open date') )
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified'), auto_now=True)

class Help(models.Model):
    def __repr__(self):
        return _('Help')

    __str__ = __repr__

    class Meta:
        verbose_name = _('Help')
        verbose_name_plural = _('Helps')

    name = models.CharField(_('Name'), default=_('Help'), max_length=10, editable=False)
    description_ios = RichTextField(_('Description iOS'))
    description_android = RichTextField(_('Description Android'))
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified'), auto_now=True)

class TermsOfService(models.Model):
    def __repr__(self):
        return _('Terms of Service')

    __str__ = __repr__

    class Meta:
        verbose_name = _('Terms of Service')
        verbose_name_plural = _('Terms of Services')

    name = models.CharField(_('Name'), default=_('Terms of Service'), max_length=10, editable=False)
    description_ios = RichTextField(_('Description iOS'))
    description_android = RichTextField(_('Description Android'))
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified'), auto_now=True)
