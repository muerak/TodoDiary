# Generated by Django 4.2.3 on 2023-07-09 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_mydiary_remove_mytodo_diary'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyDiary',
        ),
    ]
