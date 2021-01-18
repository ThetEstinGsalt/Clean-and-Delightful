from django.db import models

# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    messege = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class cardimage(models.Model):
    name = models.CharField(max_length=30)
    foods_top = models.CharField(max_length=3000)
    lifestyle_top = models.CharField(max_length=3000)
    facts_top = models.CharField(max_length=3000)
    fitness = models.CharField(max_length=3000)
    foods = models.CharField(max_length=3000)
    lifestyle = models.CharField(max_length=3000)


class contacts(models.Model):
    text = models.TextField(max_length=5000)


class about(models.Model):
    text = models.TextField(max_length=5000)


class social(models.Model):
    facebook = models.CharField(max_length=3000)
    insta = models.CharField(max_length=3000)
    mail = models.CharField(max_length=3000)
