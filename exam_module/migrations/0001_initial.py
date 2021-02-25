# Generated by Django 3.1.2 on 2021-02-25 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LabExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField()),
                ('exam_name', models.CharField(max_length=200)),
                ('exam_desc', models.TextField(max_length=500)),
                ('total_marks', models.FloatField()),
                ('pass_marks', models.FloatField()),
                ('exam_status', models.BooleanField()),
            ],
        ),
    ]
