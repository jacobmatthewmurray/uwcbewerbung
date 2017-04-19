# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-14 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgmgm', '0006_auto_20161215_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50, verbose_name='Aktivität')),
                ('activitydate', models.DateTimeField()),
                ('description', models.CharField(max_length=200)),
                ('editdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activitytype', models.CharField(max_length=20, verbose_name='Activity Type')),
                ('editdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='kontakt',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgmgm.Organisation'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='bundesland',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgmgm.Bundesland'),
        ),
        migrations.AddField(
            model_name='activity',
            name='activitytype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgmgm.ActivityType'),
        ),
        migrations.AddField(
            model_name='activity',
            name='kontakt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgmgm.Kontakt'),
        ),
        migrations.AddField(
            model_name='activity',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgmgm.Organisation'),
        ),
    ]