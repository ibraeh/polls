# Generated by Django 3.0.8 on 2020-08-07 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0011_presidentialpollresult_over_voting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presidentialpollresult',
            old_name='over_voting',
            new_name='voting_status',
        ),
    ]
