from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=250)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_user_items(cls, profile):
        items = Item.objects.filter(owner__pk=profile)
        return items


# Create your models here.
class Profile(models.Model):
    # photo = models.ImageField(upload_to='image/', null=True)
    # email = models.CharField(max_length=30, null=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, default=1)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    class Meta:
        ordering = ['user']

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


