# Generated by Django 5.0.1 on 2024-03-05 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('deptnm', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.dept')),
            ],
        ),
    ]
