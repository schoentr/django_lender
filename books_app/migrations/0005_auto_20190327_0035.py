# Generated by Django 2.1.7 on 2019-03-27 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0004_auto_20190327_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='last_borrowed',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
