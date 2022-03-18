# Generated by Django 3.2.6 on 2022-03-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_itemslist_imageofproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatingUser',
            fields=[
                ('first_name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=32, null=True)),
                ('userName', models.CharField(max_length=32, null=True)),
                ('email_address', models.EmailField(max_length=32, null=True)),
                ('mobileNumber', models.IntegerField(null=True)),
            ],
        ),
    ]