# Generated by Django 3.2.5 on 2021-07-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210724_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='age',
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
    ]
