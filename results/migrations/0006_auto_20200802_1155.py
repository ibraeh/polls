# Generated by Django 3.0.8 on 2020-08-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_auto_20200802_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presidentialpollresult',
            name='CPP',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='presidentialpollresult',
            name='NDC',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='presidentialpollresult',
            name='NPP',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
