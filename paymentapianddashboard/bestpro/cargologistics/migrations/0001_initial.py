# Generated by Django 3.2.10 on 2022-05-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=8)),
                ('username', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('passwd', models.CharField(max_length=255)),
            ],
        ),
    ]
