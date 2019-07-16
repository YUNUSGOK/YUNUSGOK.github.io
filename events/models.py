from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile
from courses.models import Course
from django.utils import timezone


class Camp(models.Model):
    date = models.DateField(default=timezone.now, verbose_name='Kamp Tarihi')
   
    #<---------------------Camp Staff------------------------------------->
    camp_ts = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='camp_ts',
        null=True, verbose_name='Kamp Teknik Sorumlusu')
    camp_ms = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='camp_ms'
        ,null=True, verbose_name='Kamp Malzeme Sorumlusu')
    camp_es = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='camp_es',
        null=True, verbose_name='Kamp Etkinlik Sorumlusu')
    camp_location = models.CharField(max_length=20,null=True,blank=True, verbose_name='Kamp Yeri')

    def __str__(self):
        return self.camp_location +"/"+str(self.date)

    def save(self, **kwargs):
        #Makes camp staff also a participant initially
        super(Camp, self).save(**kwargs)
        camp_participant1 = CampParticipant(event=self,member=self.camp_ts)
        camp_participant2 = CampParticipant(event=self,member=self.camp_es)
        camp_participant3 = CampParticipant(event=self,member=self.camp_ms)
        camp_participant1.save()
        camp_participant2.save()
        camp_participant3.save()


class Lecture(models.Model):
    date = models.DateTimeField(blank=True,null=True,default=timezone.now)
    instructor = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='instructor')
    lecture_course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='lecture_course')


class Meeting(models.Model):
    date =models.DateTimeField(blank=True,null=True,default=timezone.now)
    location = models.CharField(max_length=20,null=True,blank=True)
    subject= models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.subject +"/"+ str(self.date.date())

class CampParticipant (models.Model):
    event = models.ForeignKey(Camp, on_delete=models.CASCADE,blank=True,null=True)
    member = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return str(self.member)


class LectureParticipant (models.Model):
    event = models.ForeignKey(Lecture, on_delete=models.CASCADE,blank=True,null=True)
    member = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.member)


class MeetingParticipant (models.Model):
    event = models.ForeignKey(Meeting, on_delete=models.CASCADE,blank=True,null=True)
    member = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.member)
