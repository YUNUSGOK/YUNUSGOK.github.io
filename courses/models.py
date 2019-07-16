from django.db import models
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.text import slugify


class Course(models.Model):
    course_code = models.CharField(max_length=7)
    course_name = models.CharField(max_length=50)
    course_content = models.TextField(null=True)
    last_update = models.DateField(default=timezone.now)


    def slug(self):
        return slugify(self.course_code)

    slug=slug

    def __str__(self):
        return self.course_code

    class Meta:#In data base courses ordered by course_code
        ordering = ['course_code',]


