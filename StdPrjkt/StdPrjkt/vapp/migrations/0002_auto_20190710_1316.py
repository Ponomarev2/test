# Generated by Django 2.2.3 on 2019-07-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(max_length=120)),
                ('subjectMark', models.CharField(max_length=20)),
                ('nomerZachetki', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='nomerZachetki',
            field=models.CharField(max_length=20),
        ),
    ]