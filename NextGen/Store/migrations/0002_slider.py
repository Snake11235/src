# Generated by Django 3.2.7 on 2021-09-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]