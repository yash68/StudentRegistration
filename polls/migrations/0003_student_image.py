# Generated by Django 2.1.7 on 2019-06-05 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='studentimages'),
        ),
    ]