# Generated by Django 4.2.2 on 2023-07-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0040_alter_personaldata_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=1000)),
                ('short_description', models.CharField(max_length=50)),
            ],
        ),
    ]
