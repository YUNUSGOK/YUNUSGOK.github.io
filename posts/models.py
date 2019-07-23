from django.db import models
import datetime

class Announcement(models.Model): 
    head = models.CharField(max_length=50 , null=True , blank=True , verbose_name='Başlık')
    short_text = models.CharField(max_length=200,null=True, blank=True, verbose_name='Duyuru Açıklama' )
    text = models.TextField(null=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    image = models.ImageField( upload_to='announcements/%Y/%m/%d/' , null=True , blank=True)
    file = models.FileField( upload_to='announcements/%Y/%m/%d/', null=True ,blank=True)
    url = models.URLField(max_length=250 , blank=True , null=True )
    url_text = models.CharField(max_length=80 , null=True , blank=True , verbose_name='Url metni')
    youtube = models.URLField(max_length=250 , blank=True , null=True )


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