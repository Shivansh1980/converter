# Generated by Django 3.1.4 on 2021-01-02 21:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('encryptfiles', '0005_encryptedfile_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encryptedfile',
            name='username',
        ),
        migrations.AddField(
            model_name='encryptedfile',
            name='useremail',
            field=models.EmailField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='encryptedfile',
            name='key',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
