# Generated by Django 3.0.4 on 2020-03-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
