# Generated by Django 3.1.3 on 2021-01-14 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_cardimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardimage',
            name='facts_top',
            field=models.CharField(default='', max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardimage',
            name='foods_top',
            field=models.CharField(default='', max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardimage',
            name='lifestyle_top',
            field=models.CharField(default='', max_length=3000),
            preserve_default=False,
        ),
    ]
