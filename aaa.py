from accounts.models import Profile 
from django.contrib.auth.models import User

def func():
    f= open('names.txt','r')
    x=[]
    for i in f:

           
        a=i.split()

        if(len(a)==4):
            a[0]+=' ' + a[1]
            del a[1]
        if(len(a)==3):
            try:
                a[2]=int(a[2])
            except:
                a[0]+=' ' + a[1]
                del a[1]
            

        first_name = a[0]
        last_name = a[1]
            
        password ='odtusat1985'
        if( len(a)==3):
            id = int(a[2])
            a[2] = int(a[2])
            if(a[2]<10):
                username = 'SAT00'+str(a[2])
            elif(a[2]<100):
                username = 'SAT0'+ str(a[2])
            elif(a[2]<1000):
                username = 'SAT' +str(a[2])


            
            user=User(id=id,username=username,first_name=first_name, last_name=last_name)


        
        user.set_password(password)
        user.save()
    f.close()
def member_no():
    for user in User.objects.all():
        user.profile.member_no=user.id
        user.profile.save()
        user.save()
def f():
    f= open('dates.txt','r')
    x=[]
    for i in f:

           
        a=i.split()
        if(len(a)==2):
            profile = Profile.objects.get(member_no=int(a[0]))
            
            profile.date = a[1] 
            profile.save()
            
    f.close()