# Generated by Django 4.0.4 on 2022-06-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0003_userhistory_prediction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='prediction',
            field=models.CharField(max_length=50),
        ),
    ]