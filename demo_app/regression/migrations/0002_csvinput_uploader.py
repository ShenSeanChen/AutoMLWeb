# Generated by Django 3.1.5 on 2021-01-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regression', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvinput',
            name='uploader',
            field=models.CharField(default='edwin', max_length=20),
            preserve_default=False,
        ),
    ]
