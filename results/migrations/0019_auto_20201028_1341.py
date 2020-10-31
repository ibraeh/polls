# Generated by Django 3.0.8 on 2020-10-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0018_auto_20200904_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presidentialpollresult',
            name='sheet',
        ),
        migrations.AddField(
            model_name='presidentialpollresult',
            name='APC',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='presidentialpollresult',
            name='GCPP',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='presidentialpollresult',
            name='GFP',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='presidentialpollresult',
            name='GUM',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='presidentialpollresult',
            name='IND',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='presidentialpollresult',
            name='LPG',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='presidentialpollresult',
            name='NDP',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='presidentialpollresult',
            name='PNC',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='presidentialpollresult',
            name='PPP',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='presidentialpollresult',
            name='pink_sheet',
            field=models.FileField(help_text='Snap and upload image of the pink sheet', upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
