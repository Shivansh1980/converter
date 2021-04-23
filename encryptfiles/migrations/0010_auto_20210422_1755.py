# Generated by Django 3.2 on 2021-04-22 17:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('encryptfiles', '0009_alter_encryptedfile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encryptedfile',
            old_name='encrypted_file',
            new_name='my_file',
        ),
        migrations.RemoveField(
            model_name='decryptedfile',
            name='useremail',
        ),
        migrations.AddField(
            model_name='decryptedfile',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
