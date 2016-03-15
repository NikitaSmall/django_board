from __future__ import unicode_literals

from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=255)
    protected = models.BooleanField(default=False)

    pub_date = models.DateTimeField('publish date', auto_now_add=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Subcategory(models.Model):
    class Meta:
        verbose_name_plural = 'subcategories'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    pub_date = models.DateTimeField('publish date', auto_now_add=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Topic(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    docfile = models.FileField(upload_to='topics/', null=True)

    pub_date = models.DateTimeField('publish date', auto_now_add=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Message(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    text = models.TextField()
    docfile = models.FileField(upload_to='messages/', null=True)

    pub_date = models.DateTimeField('publish date', auto_now_add=True)

    def __str__(self):
        return self.text
