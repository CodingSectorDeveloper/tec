# Generated by Django 4.0.4 on 2022-05-27 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_regionaladmin_zonaladmin_remove_student_branch_admin_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]