# Generated by Django 3.2.6 on 2022-03-18 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_creatinguser'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatinguser',
            name='password',
            field=models.CharField(max_length=32, null=True),
        ),
    ]