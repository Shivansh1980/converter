# Generated by Django 3.2 on 2021-04-23 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encryptfiles', '0011_auto_20210423_1250'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DecryptedFile',
        ),
    ]