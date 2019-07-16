from django.db import models
import datetime

class Announcement(models.Model): 
    head = models.CharField(max_length=50 , null=True , blank=True , verbose_name='Başlık')
    text = models.TextField(null=True)
    date = models.DateField(default=datetime.date.today)


class AnnouncementImage(models.Model):
    announcement = models.ForeignKey( Announcement ,  on_delete=models.CASCADE , blank=True , null=True )
    image = models.ImageField( upload_to='announcements/%Y/%m/%d/' , null=True)


class AnnouncementFile(models.Model):
    announcement = models.ForeignKey( Announcement ,  on_delete=models.CASCADE , blank=True , null=True )
    file = models.FileField( upload_to='announcements/%Y/%m/%d/', null=True )


class AnnouncementUrl(models.Model):
    announcement = models.ForeignKey( Announcement ,  on_delete=models.CASCADE , blank=True , null=True )
    file = models.URLField(max_length=250 , blank=True , null=True )


class About(models.Model):
    text =  models.TextField(null=True)
    image = models.ImageField( upload_to='about/%Y/%m/%d/' , null=True)


class Photo(models.Model):
    head = models.CharField(max_length=80,null=True)
    text = models.TextField(null=True)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/' , null=True)