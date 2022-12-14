# Generated by Django 4.0.4 on 2022-05-27 04:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('password', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('admission_fee', models.IntegerField()),
                ('monthly_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MidAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('password', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('password', models.TextField()),
                ('role', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('password', models.TextField()),
                ('father_name', models.TextField()),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('money2pay', models.IntegerField()),
                ('money_paid', models.IntegerField()),
                ('no_due', models.BooleanField(default=True)),
                ('student_id', models.IntegerField()),
                ('branch_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.branchadmin')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
        ),
    ]
