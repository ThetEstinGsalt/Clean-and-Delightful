# Generated by Django 3.1.3 on 2021-01-14 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fitness', models.CharField(max_length=3000)),
                ('foods', models.CharField(max_length=3000)),
                ('lifestyle', models.CharField(max_length=3000)),
            ],
        ),
    ]
