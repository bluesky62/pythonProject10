# Generated by Django 4.0.2 on 2022-02-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('For', models.CharField(max_length=30)),
                ('project', models.TextField(max_length=50)),
            ],
        ),
    ]
