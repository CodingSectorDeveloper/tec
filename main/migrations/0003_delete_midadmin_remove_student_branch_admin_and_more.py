# Generated by Django 4.0.4 on 2022-05-27 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_branchadmin_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MidAdmin',
        ),
        migrations.RemoveField(
            model_name='student',
            name='branch_admin',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.DeleteModel(
            name='SubAdmin',
        ),
        migrations.DeleteModel(
            name='BranchAdmin',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
