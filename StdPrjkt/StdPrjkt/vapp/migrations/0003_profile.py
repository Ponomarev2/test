# Generated by Django 2.2.3 on 2019-07-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0002_auto_20190710_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(max_length=120)),
                ('subjectMark', models.CharField(max_length=20)),
                ('nomerZachetki', models.CharField(max_length=20)),
            ],
        ),
    ]
