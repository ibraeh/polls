# Generated by Django 3.0.8 on 2020-08-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0006_auto_20200802_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presidentialpollresult',
            name='CPP',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='presidentialpollresult',
            name='NDC',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='presidentialpollresult',
            name='NPP',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='presidentialpollresult',
            name='rejected',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]
