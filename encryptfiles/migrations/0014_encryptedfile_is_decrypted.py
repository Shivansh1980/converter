# Generated by Django 3.2 on 2021-04-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encryptfiles', '0013_alter_encryptedfile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='encryptedfile',
            name='is_decrypted',
            field=models.BooleanField(default=False),
        ),
    ]
