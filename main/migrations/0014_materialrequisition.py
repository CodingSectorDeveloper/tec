# Generated by Django 4.0.4 on 2022-05-31 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_materialentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialRequisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bag', models.IntegerField()),
                ('pen', models.IntegerField()),
                ('id_card', models.IntegerField()),
                ('uniform', models.IntegerField()),
                ('date_issued', models.DateField(auto_now_add=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.branchadmin')),
            ],
        ),
    ]
