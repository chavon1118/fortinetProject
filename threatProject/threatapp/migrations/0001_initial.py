# Generated by Django 2.1.dev20180216185855 on 2018-02-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='record date')),
                ('filename', models.CharField(max_length=128)),
                ('action', models.CharField(max_length=128)),
                ('submit_type', models.CharField(max_length=128)),
                ('rating', models.CharField(max_length=128)),
            ],
        ),
    ]
