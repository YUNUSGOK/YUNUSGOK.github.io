from django.contrib import admin
from events.models import  Lecture, Meeting 
from accounts.models import  TakenCourse ,Profile ,SignUpRequest
from courses.models import Course
from django.contrib.auth.models import User , Group

#Model object foreignkey addition in admin panel
class CourseInline(admin.StackedInline):
    model= TakenCourse
    extra = 3

#Model object create/update view field set view in admin panel
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personel Info',               {'fields': ['member_no','user','phone','birth_date','blood_type']}),
        ('Diver Info ', {'fields': ['dive_count','dive_level','photo','date']}),]

    inlines =[CourseInline]


admin.site.register(Profile,ProfileAdmin)
admin.site.register(Lecture)
admin.site.register(Meeting)
admin.site.register(SignUpRequest)
