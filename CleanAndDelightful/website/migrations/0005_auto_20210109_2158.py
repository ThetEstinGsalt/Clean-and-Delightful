# Generated by Django 3.1.3 on 2021-01-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210109_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
