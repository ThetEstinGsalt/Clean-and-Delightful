from django.db import models

# Create your models here.


class Blog(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="")
    thumbnail = models.CharField(max_length=3000, default="")
    concept = models.CharField(max_length=10000, default="")
    overview = models.CharField(max_length=500, default="")
    keywords = models.CharField(max_length=500, default="")
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

    article_title3 = models.CharField(max_length=100, blank=True, default="")
    image3 = models.CharField(max_length=3000, blank=True, default="")
    article_content3 = models.CharField(
        max_length=10000, blank=True, default="")

    article_title4 = models.CharField(max_length=100, blank=True, default="")
    image4 = models.CharField(max_length=3000, blank=True, default="")
    article_content4 = models.CharField(
        max_length=10000, blank=True, default="")
    article_title5 = models.CharField(max_length=100, blank=True, default="")
    image5 = models.CharField(max_length=3000, blank=True, default="")
    article_content5 = models.CharField(
        max_length=10000, blank=True, default="")
    article_title6 = models.CharField(max_length=100, blank=True, default="")
    image6 = models.CharField(max_length=3000, blank=True, default="")
    article_content6 = models.CharField(
        max_length=10000, blank=True, default="")
    article_title7 = models.CharField(max_length=100, blank=True, default="")
    image7 = models.CharField(max_length=3000, blank=True, default="")
    article_content7 = models.CharField(
        max_length=10000, blank=True, default="")
    article_title8 = models.CharField(max_length=100, blank=True, default="")
    image8 = models.CharField(max_length=3000, blank=True, default="")
    article_content8 = models.CharField(
        max_length=10000, blank=True, default="")
    article_title9 = models.CharField(max_length=100, blank=True, default="")
    image9 = models.CharField(max_length=3000, blank=True, default="")
    article_content9 = models.CharField(
        max_length=10000, blank=True, default="")
    article_title10 = models.CharField(max_length=100, blank=True, default="")
    image10 = models.CharField(max_length=3000, blank=True, default="")
    article_content10 = models.CharField(
        max_length=10000, blank=True, default="")
    article_title11 = models.CharField(max_length=100, blank=True, default="")
    image11 = models.CharField(max_length=3000, blank=True, default="")
    article_content11 = models.CharField(
        max_length=10000, blank=True, default="")
    article_title12 = models.CharField(max_length=100, blank=True, default="")
    image12 = models.CharField(max_length=3000, blank=True, default="")
    article_content12 = models.CharField(
        max_length=10000, blank=True, default="")
    article_title13 = models.CharField(max_length=100, blank=True, default="")
    image13 = models.CharField(max_length=3000, blank=True, default="")
    article_content13 = models.CharField(
        max_length=10000, blank=True, default="")
    article_title14 = models.CharField(max_length=100, blank=True, default="")
    image14 = models.CharField(max_length=3000, blank=True, default="")
    article_content14 = models.CharField(
        max_length=10000, blank=True, default="")
    article_title15 = models.CharField(max_length=100, blank=True, default="")
    image15 = models.CharField(max_length=3000, blank=True, default="")
    article_content15 = models.CharField(
        max_length=10000, blank=True, default="")

    def __str__(self):
        return self.title
