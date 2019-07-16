from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from courses.models import Course 
from django.db.models.signals import post_save

"""To check user registry to limit access to personal informatons, unregistered
visiters can create an SignUpRequest. 
Authorized user can approve or disapprove these requests"""
class SignUpRequest( models.Model ):
    username = models.CharField( max_length=32 )
    first_name =models.CharField( max_length=32 )
    last_name =models.CharField( max_length=32 )
    email = models.EmailField(  )
    password1 = models.CharField( max_length = 32 , null=True , blank=True , verbose_name='Şifre:' )
    password2 = models.CharField( max_length = 32 , null=True , blank=True , verbose_name='Şifreyi Tekrar Giriniz:' )
    member_no = models.IntegerField( null=True , blank=True )



def pp_image(instance, filename):
    #pp_images gives folder path where folder name is member_no 
    return 'pp/%s/%s' % (instance.member_no, filename)



class Profile( models.Model ):
    """
    Profile is extended model of User that can take extra information such as
    personal info ,contact info...
    """
    #blood types
    types = [
            ("0 Rh+" ,"0 Rh+") , ("A Rh+" , "A Rh+") , 
            ("B Rh+" , "B Rh+") , ("AB Rh+", "AB Rh+") , 
            ("0 Rh-" , "0 Rh-") , ("A Rh-" , "A Rh-") , 
            ("B Rh-" , "B Rh-") , ("AB Rh-", "AB Rh-") ,
        ]
    #Diving levels 
    levels = [
                ("Temel","Temel"), 
                ("İleri","İleri"),
                ("Kurtarma","Kurtarma")
            ] 

    member_no = models.IntegerField( null=True , blank=True ,unique=True)
    user = models.OneToOneField( User ,  on_delete=models.CASCADE , blank=True , null=True )
    phone =  models.CharField( max_length=10 , null=True , blank=True )
    dive_count = models.IntegerField( blank=True , null=True )
    dive_level = models.CharField(max_length=20,choices=levels,null=True)
    blood_type= models.CharField( max_length=7 , choices=types , null=True , blank=True )
    birth_date = models.DateField( null=True , blank=True )
    photo = models.ImageField( upload_to=pp_image, default='pp/default_pp.svg' )
    date = models.CharField( max_length=7, null=True , blank=True )
    department = models.CharField( max_length=7, null=True , blank=True, verbose_name='Bölüm' )

    class Meta:
        ordering =( 'member_no' ,  )

    def __str__ ( self ):
        return self.user.first_name + " " + self.user.last_name


class TakenCourse( models.Model ):
    """
    TakenCourse links Profile model and Course model in courses to display
    members previous courses and which courses can be taken
    """
    taken_date = models.DateField( null=True , blank=True )
    student = models.ForeignKey( Profile ,  on_delete=models.CASCADE , blank=True , null=True )
    course =models.OneToOneField( Course , on_delete=models.CASCADE , null=True , blank=True )

    def __str__( self ):
        return self.course.course_name

    class Meta:
        ordering = ['course']


@receiver( post_save , sender=User )
def create_user_profile( sender ,  instance ,  created ,  **kwargs ):
    if created:
        Profile.objects.create( user=instance )


@receiver( post_save ,  sender=User )
def save_user_profile( sender ,  instance ,  **kwargs ):
    instance.profile.save(  )


