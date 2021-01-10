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


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="")
    thumbnail = models.CharField(max_length=3000, default="")
    concept = models.CharField(max_length=10000, default="")
    article_title = models.CharField(max_length=100, default="")
    image = models.CharField(max_length=3000, default="")
    article_content = models.CharField(max_length=10000, default="")

    article_title1 = models.CharField(max_length=100, blank=True, default="")
    image1 = models.CharField(max_length=3000, blank=True, default="")
    article_content1 = models.CharField(
        max_length=10000, blank=True, default="")

    article_title2 = models.CharField(max_length=100, blank=True, default="")
    image2 = models.CharField(max_length=3000, blank=True, default="")
    article_content2 = models.CharField(
        max_length=10000, blank=True, default="")

    def __str__(self):
        return self.title
