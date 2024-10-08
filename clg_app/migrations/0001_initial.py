# Generated by Django 5.0.7 on 2024-08-27 16:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Addcourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=50)),
                ('coursefee', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('date', models.DateField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clg_app.addcourse')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('age', models.IntegerField(null=True)),
                ('contact', models.CharField(max_length=10)),
                ('img', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clg_app.addcourse')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
