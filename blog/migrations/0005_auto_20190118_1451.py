# Generated by Django 2.1.1 on 2019-01-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190118_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(),
        ),
    ]
