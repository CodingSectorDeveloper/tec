# Generated by Django 4.0.4 on 2022-06-01 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_materialrequisition'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='registration_fee',
            field=models.IntegerField(default=1000),
        ),
    ]
