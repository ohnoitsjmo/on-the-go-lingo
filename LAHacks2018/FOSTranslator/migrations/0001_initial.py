# Generated by Django 2.0.3 on 2018-03-31 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idiom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idiom', models.CharField(max_length=400)),
                ('definition', models.CharField(max_length=1000)),
            ],
        ),
    ]