# Generated by Django 3.0.9 on 2020-08-15 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_photo', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('facebook_link', models.CharField(blank=True, max_length=300)),
                ('instagram_link', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_img', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
        ),
    ]
