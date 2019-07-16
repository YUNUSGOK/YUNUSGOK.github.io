from django.contrib import admin

# Register your models here.
from events.models import Camp , CampParticipant


class CampParticipantInline(admin.StackedInline):
    #Camp editing page in admin panel 3 and participants can be added. 
	model = CampParticipant
	extra = 3


class CampAdmin(admin.ModelAdmin):
	fieldsets = [
        ('Kamp Bilgileri',               {'fields': ['date','camp_location']}),
        ('Sorumlular ', {'fields':['camp_ts','camp_ms','camp_es']}),
        ]
        
	inlines=[CampParticipantInline]


admin.site.register(Camp,CampAdmin)
admin.site.register(CampParticipant)
