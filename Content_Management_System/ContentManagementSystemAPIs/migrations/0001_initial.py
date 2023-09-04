# Generated by Django 4.1.1 on 2023-09-03 11:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=500, null=True, validators=[django.core.validators.RegexValidator(message="Email Id must be entered in the format: example326@gmail.com' Up to 50 character allowed.", regex='^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$')])),
                ('Password', models.CharField(max_length=20, null=True)),
                ('Full_Name', models.CharField(max_length=100, null=True)),
                ('Phone', models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '999999999',0989279999 Up to 10 digits allowed.", regex='^(\\+91[\\-\\s]?)?[0]?(91)?\\d{9}$')])),
                ('Address', models.CharField(max_length=500)),
                ('City', models.CharField(max_length=500)),
                ('State', models.CharField(max_length=500)),
                ('Country', models.CharField(max_length=500)),
                ('Pincode', models.IntegerField(max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30, null=True)),
                ('Body', models.CharField(max_length=60, null=True)),
                ('Document', models.FileField(null=True, upload_to='')),
                ('Categories', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
