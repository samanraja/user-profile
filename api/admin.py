from django.contrib import admin

from .models import User, UserProfile, Hobbies, Address

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Hobbies)
admin.site.register(Address)
