from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Person)


class SkillAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'skill',
    ]
    list_filter = ('user','skill')

admin.site.register(Skills, SkillAdmin)

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'social_media',
    ]
    list_filter = ('user','social_media')
   
admin.site.register(SocialMedia, SocialMediaAdmin)

