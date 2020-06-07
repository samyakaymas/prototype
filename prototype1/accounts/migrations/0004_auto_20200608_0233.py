# Generated by Django 3.0.7 on 2020-06-07 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200608_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.AddField(
            model_name='user',
            name='is_permitted',
            field=models.BooleanField(default=False),
        ),
    ]
