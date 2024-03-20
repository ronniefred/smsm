# Generated by Django 4.2.11 on 2024-03-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('FirstName', models.CharField(max_length=15)),
                ('LastName', models.CharField(max_length=20)),
                ('Course', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=30)),
                ('Enquiry_date', models.DateField()),
                ('starting_date', models.DateField()),
                ('Phone', models.CharField(max_length=20)),
            ],
        ),
    ]
