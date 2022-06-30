from django.db import models
from django.shortcuts import render
from django.db.models.fields import TextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField 

# creating model Menu
class MenuPage(models.Model):
    title = models.CharField('Tytuł',max_length=20)
    bodytext = RichTextUploadingField('pole tekstowe')
    class Meta:
        verbose_name = 'Strona menu'
        verbose_name_plural = "Strony menu"
    def __str__(self):
        return self.title

# creating model manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

# post model
class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title = models.CharField('Tytuł',max_length=250)
    slug = models.SlugField('skrót',max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body=RichTextUploadingField('pole tekstowe') 

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=14,choices=STATUS_CHOICES,default='szkic')    
    thumbnail = models.ImageField('miniaturka',upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="320" height="180" />'.format(self.thumbnail.url))
        return ""

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Wpis aktualności'
        verbose_name_plural = "Wpisy aktualności"
    
    def __str__(self):
        return self.title
    objects = models.Manager() 
    published = PublishedManager() 

    def get_absolute_url(self):
        return reverse('ccms_site:post_detail',args=[self.slug])


    
