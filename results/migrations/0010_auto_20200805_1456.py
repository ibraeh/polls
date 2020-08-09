# Generated by Django 3.0.8 on 2020-08-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0009_presidentialpollresult_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='presidentialpollresult',
            name='valid_votes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='presidentialpollresult',
            name='vote_cast',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='constituency',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='electoralarea',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='electoralarea',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='pollingstation',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='pollingstation',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Polling Station Name'),
        ),
        migrations.AlterField(
            model_name='presidentialpollresult',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
