# Generated by Django 3.2 on 2022-12-18 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_book_date_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='secret_name',
            field=models.CharField(default='default', max_length=256),
            preserve_default=False,
        ),
    ]
