# Generated by Django 3.0.7 on 2020-08-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0007_auto_20200810_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='gameInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamename', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]