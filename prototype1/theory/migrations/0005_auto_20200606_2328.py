# Generated by Django 3.0.7 on 2020-06-06 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theory', '0004_auto_20200606_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theory',
            old_name='Concept',
            new_name='concept',
        ),
    ]
