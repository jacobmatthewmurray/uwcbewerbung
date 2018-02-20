# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-20 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgmgm', '0012_auto_20180220_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rescource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Resource Titel')),
                ('link', models.URLField(verbose_name='Link')),
                ('linktitle', models.CharField(max_length=100, verbose_name='Link Titel')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='activity',
            name='kontakt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgmgm.Kontakt', verbose_name='Kontakt'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgmgm.Organisation', verbose_name='Organisation'),
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
    ]