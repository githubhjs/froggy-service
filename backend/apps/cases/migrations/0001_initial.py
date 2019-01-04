# Generated by Django 2.1.4 on 2019-01-04 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=6, verbose_name='Case Number')),
                ('title', models.CharField(max_length=255, verbose_name='Case Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('mobile', models.CharField(max_length=10, verbose_name='Mobile')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('open_time', models.DateTimeField(blank=True, null=True, verbose_name='Opened Time')),
                ('close_time', models.DateTimeField(blank=True, null=True, verbose_name='Closed Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Time')),
            ],
            options={
                'verbose_name': 'Case',
                'verbose_name_plural': 'Cases',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='CaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=6, verbose_name='Case Number')),
                ('title', models.CharField(max_length=255, verbose_name='Case Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('mobile', models.CharField(max_length=10, verbose_name='Mobile')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('open_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Opened Time')),
                ('close_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Closed Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Time')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_histories', to='cases.Case', verbose_name='Case')),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case_histories', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'Case History',
                'verbose_name_plural': 'Case Histories',
                'ordering': ('-update_time',),
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Time')),
            ],
            options={
                'verbose_name': 'User Region',
                'verbose_name_plural': 'User Region',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Time')),
            ],
            options={
                'verbose_name': 'Case Status',
                'verbose_name_plural': 'Case Status',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Time')),
            ],
            options={
                'verbose_name': 'Case Type',
                'verbose_name_plural': 'Case Type',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='casehistory',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_histories', to='cases.Region', verbose_name='User Region'),
        ),
        migrations.AddField(
            model_name='casehistory',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_histories', to='cases.Status', verbose_name='Case Status'),
        ),
        migrations.AddField(
            model_name='casehistory',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_histories', to='cases.Type', verbose_name='Case Type'),
        ),
        migrations.AddField(
            model_name='case',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='cases.Region', verbose_name='User Region'),
        ),
        migrations.AddField(
            model_name='case',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='cases.Status', verbose_name='Case Status'),
        ),
        migrations.AddField(
            model_name='case',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='cases.Type', verbose_name='Case Type'),
        ),
    ]