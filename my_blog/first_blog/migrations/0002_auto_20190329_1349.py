# Generated by Django 2.1.7 on 2019-03-29 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]