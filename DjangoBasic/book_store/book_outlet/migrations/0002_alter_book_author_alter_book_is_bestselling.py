# Generated by Django 5.1.7 on 2025-03-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_bestselling',
            field=models.BooleanField(default=False),
        ),
    ]
