# Generated by Django 4.2.2 on 2023-07-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_alter_personaldata_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='url',
            field=models.URLField(),
        ),
    ]
