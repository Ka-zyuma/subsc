# Generated by Django 3.0.5 on 2020-06-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscapp', '0008_subsc_dateleft'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsc',
            name='username',
            field=models.CharField(default='akashikazuma', max_length=100),
        ),
    ]
