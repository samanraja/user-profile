from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    hobbies = models.ManyToManyField('Hobbies', related_name='user_profile', blank=True)

    def default_address(self):
        address = self.address.get(is_default=True)
        return address.address


def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)


class Hobbies(models.Model):
    hobby_name = models.CharField(max_length=255, blank=True, null=True)


class Address(models.Model):
    profile = models.ForeignKey(UserProfile, related_name='address', on_delete=models.CASCADE,
                                null=True, blank=True)
    address = models.CharField(max_length=255, )
    is_default = models.BooleanField(default=False)


def set_default_address(sender, instance, **kwargs):
    if instance:
        if instance.is_default:
            Address.objects.filter(profile=instance.profile, is_default=True).update(is_default=False)
            Address.objects.filter(id=instance.id).update(is_default=True)


pre_save.connect(set_default_address, sender=Address)
