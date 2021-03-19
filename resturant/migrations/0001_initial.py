# Generated by Django 2.1 on 2019-08-31 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('photo_branch', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
            options={
                'db_table': 'branches',
            },
        ),
        migrations.CreateModel(
            name='HallMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_type', models.CharField(max_length=100)),
                ('charges_per_head', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'hallmeal',
            },
        ),
        migrations.CreateModel(
            name='Halls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo_hall', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('size', models.CharField(max_length=200)),
                ('capacity', models.CharField(max_length=100)),
                ('charges_per_head', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('branch_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resturant.Branches')),
            ],
            options={
                'db_table': 'halls',
            },
        ),
    ]