# Generated by Django 4.0.4 on 2022-05-28 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_student_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='admission_fee',
            new_name='addmission_fee',
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.TextField(blank=True),
        ),
    ]