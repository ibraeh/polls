# Generated by Django 3.0.8 on 2020-07-29 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Constituency',
                'verbose_name_plural': 'Constituencies',
            },
        ),
        migrations.CreateModel(
            name='ElectoralArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('constituency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.Constituency')),
            ],
        ),
        migrations.CreateModel(
            name='PollingStation',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='Polling Station Name')),
                ('pscode', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True, verbose_name='Polling Station Code')),
                ('voter_pop', models.PositiveSmallIntegerField(verbose_name='Voter Population')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('constituency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.Constituency')),
                ('electoral_area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.ElectoralArea')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('vote', models.CharField(max_length=10)),
                ('photo', models.FileField(help_text='upload photos here', upload_to='vote')),
            ],
        ),
        migrations.CreateModel(
            name='PollResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NDC', models.CharField(max_length=8)),
                ('NPP', models.CharField(max_length=8)),
                ('CPP', models.CharField(max_length=8)),
                ('pink_sheet', models.FileField(help_text='Snap and upload image of the sheet', upload_to='uploads/%Y/%m/%d/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('pscode', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='results.PollingStation', verbose_name='Polling Station')),
            ],
        ),
        migrations.AddField(
            model_name='pollingstation',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.Region'),
        ),
        migrations.AddField(
            model_name='constituency',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.Region'),
        ),
    ]
