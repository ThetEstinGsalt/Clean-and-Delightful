from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Blog(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="")
    thumbnail = models.CharField(max_length=3000, default="")
    concept = models.CharField(max_length=10000, default="")
    overview = models.CharField(max_length=500, default="")
    categories = models.ManyToManyField(Category)
    article_title = models.CharField(max_length=100, default="")
    image = models.CharField(max_length=3000, default="")
    article_content = models.TextField(max_length=10000, default="")

    article_title1 = models.CharField(max_length=100, blank=True, default="")
    image1 = models.CharField(max_length=3000, blank=True, default="")
    article_content1 = models.TextField(
        max_length=10000, blank=True, default="")

    article_title2 = models.CharField(max_length=100, blank=True, default="")
    image2 = models.CharField(max_length=3000, blank=True, default="")
    article_content2 = models.TextField(
        max_length=10000, blank=True, default="")

    article_title3 = models.CharField(max_length=100, blank=True, default="")
    image3 = models.CharField(max_length=3000, blank=True, default="")
    article_content3 = models.TextField(
        max_length=10000, blank=True, default="")

    article_title4 = models.CharField(max_length=100, blank=True, default="")
    image4 = models.CharField(max_length=3000, blank=True, default="")
    article_content4 = models.TextField(
        max_length=10000, blank=True, default="")
    article_title5 = models.CharField(max_length=100, blank=True, default="")
    image5 = models.CharField(max_length=3000, blank=True, default="")
    article_content5 = models.TextField(
        max_length=10000, blank=True, default="")
    article_title6 = models.CharField(max_length=100, blank=True, default="")
    image6 = models.CharField(max_length=3000, blank=True, default="")
    article_content6 = models.TextField(
        max_length=10000, blank=True, default="")
    article_title7 = models.CharField(max_length=100, blank=True, default="")
    image7 = models.CharField(max_length=3000, blank=True, default="")
    article_content7 = models.TextField(
        max_length=10000, blank=True, default="")
    article_title8 = models.CharField(max_length=100, blank=True, default="")
    image8 = models.CharField(max_length=3000, blank=True, default="")
    article_content8 = models.TextField(
        max_length=10000, blank=True, default="")
    article_title9 = models.CharField(max_length=100, blank=True, default="")
    image9 = models.CharField(max_length=3000, blank=True, default="")
    article_content9 = models.TextField(
        max_length=10000, blank=True, default="")
    article_title10 = models.CharField(max_length=100, blank=True, default="")
    image10 = models.CharField(max_length=3000, blank=True, default="")
    article_content10 = models.TextField(
        max_length=10000, blank=True, default="")
    article_title11 = models.CharField(max_length=100, blank=True, default="")
    image11 = models.CharField(max_length=3000, blank=True, default="")
    article_content11 = models.TextField(
        max_length=10000, blank=True, default="")
    article_title12 = models.CharField(max_length=100, blank=True, default="")
    image12 = models.CharField(max_length=3000, blank=True, default="")
    article_content12 = models.TextField(
        max_length=10000, blank=True, default="")
    article_title13 = models.CharField(max_length=100, blank=True, default="")
    image13 = models.CharField(max_length=3000, blank=True, default="")
    article_content13 = models.TextField(
        max_length=10000, blank=True, default="")
    article_title14 = models.CharField(max_length=100, blank=True, default="")
    image14 = models.CharField(max_length=3000, blank=True, default="")
    article_content14 = models.TextField(
        max_length=10000, blank=True, default="")
    article_title15 = models.CharField(max_length=100, blank=True, default="")
    image15 = models.CharField(max_length=3000, blank=True, default="")
    article_content15 = models.TextField(
        max_length=10000, blank=True, default="")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class affiliate(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    name2 = models.CharField(max_length=100)
    image2 = models.CharField(max_length=1000)
    link2 = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
