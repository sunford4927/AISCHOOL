from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    like1 = models.CharField(max_length=10)
    like2 = models.CharField(max_length=10)
    like3 = models.CharField(max_length=10)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Page.objects.create(user=instance)


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    foodname = models.TextField()
    price = models.IntegerField()
    class Meta:
        db_table = 'menu'


class location(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    score = models.TextField()
    category = models.TextField()
    class Meta:
        db_table = 'location'

class foodends(models.Model):
    foodname = models.TextField()
    price = models.IntegerField()
    score = models.TextField()
    name = models.CharField(max_length=255)
    location = models.TextField()
    category = models.TextField()

    class Meta:
        db_table = 'foodends'

class koreafoods(models.Model):
    foodname = models.TextField()
    price = models.IntegerField()
    score = models.TextField()
    name = models.CharField(max_length=255)
    location = models.TextField()
    category = models.TextField()

    class Meta:
        db_table = 'koreafoods'