# Generated by Django 2.0.5 on 2018-05-14 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verse',
            old_name='chapter_int',
            new_name='chapter',
        ),
        migrations.RenameField(
            model_name='verse',
            old_name='verse_int',
            new_name='verse',
        ),
    ]
