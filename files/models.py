# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
import misaka

User = get_user_model()


# Create your models here.
class File(models.Model):
    user = models.ForeignKey(User, related_name='files')
    created_at = models.DateTimeField(auto_now=True)
    datafile = models.FileField(
        storage=settings.MEDIA_DIR,
        upload_to='images/',
        default='settings.MEDIA_DIR/images/py_django.png'
    )

    def __str__(self):
        return self.datafile

    def get_absolute_url(self):
        return reverse('files:single', kwargs={'username':self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'datafile']

