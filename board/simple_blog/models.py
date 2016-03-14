from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'sategories'

    name = models.CharField(max_length=255)
    protected = models.BooleanField(default=False)

    pub_date = models.DateTimeField('publish date', auto_now_add=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    class Meta:
        verbose_name_plural = 'subcategories'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    pub_date = models.DateTimeField('publish date', auto_now_add=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    pub_date = models.DateTimeField('publish date', auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    text = models.TextField()

    pub_date = models.DateTimeField('publish date', auto_now_add=True)

    def __str__(self):
        return self.text
