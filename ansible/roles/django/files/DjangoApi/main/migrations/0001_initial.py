# Generated by Django 4.1.2 on 2022-10-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeName', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('DateOdJoining', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=100)),
            ],
        ),
    ]