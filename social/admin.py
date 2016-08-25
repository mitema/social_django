from django.contrib import admin

# Register your models here.

from social.models import Profile, Member

admin.site.register(Profile)
admin.site.register(Member)
