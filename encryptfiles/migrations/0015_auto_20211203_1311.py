# Generated by Django 3.1.4 on 2021-12-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encryptfiles', '0014_encryptedfile_is_decrypted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryptedfile',
            name='my_file',
            field=models.FileField(upload_to=':\\Users\\ASUS\\Desktop\\Projects And Development\\Projects\\converter\\static/media/'),
        ),
    ]
