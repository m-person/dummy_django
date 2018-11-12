import os
import uuid

from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnStoragePlaceholderImage


def upload_to_filename(obj, filename):
    return '{}{}'.format(uuid.uuid4(), (os.path.splitext(filename))[1])


class Article(models.Model):
    title = models.CharField('Title', max_length=128, default='')
    slug = models.SlugField('Slug', unique=True)
    body = models.TextField('Article body', blank=True, null=True)
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)
    image = VersatileImageField(
        'Image',
        upload_to=upload_to_filename,
        placeholder_image=OnStoragePlaceholderImage(path='placeholder-image.png'),
        blank=True,
        null=True)

    def __str__(self):
        return self.title or ''

    def get_absolute_url(self):
        return reverse_lazy('article_details', kwargs={'slug': self.slug})

    def _get_slug(self):
        if not self.title:
            new_slug = slugify(uuid.uuid4())
        else:
            slug = slugify(self.title)
            suf = 0
            new_slug = slug
            while Article.objects.exclude(id=self.id).filter(slug=new_slug).exists():
                suf += 1
                new_slug = '{}-{}'.format(slug, suf)

        return new_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_slug()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
