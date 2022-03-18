# Generated by Django 3.2.6 on 2022-03-17 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryName', models.CharField(max_length=254, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brandName', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('brandCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.category')),
            ],
        ),
    ]
