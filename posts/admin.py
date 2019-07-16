from django.contrib import admin

# Register your models here.
from .models import Announcement , AnnouncementImage,  About ,Photo



admin.site.register(Announcement)
admin.site.register(AnnouncementImage)
admin.site.register(About)
admin.site.register(Photo)