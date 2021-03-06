# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-21 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgmgm', '0017_merge_20180221_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='kontakt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgmgm.Kontakt', verbose_name='Kontakt'),
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
        migrations.AlterField(
            model_name='organisation',
            name='plz',
            field=models.CharField(max_length=20, verbose_name='Postleitzahl'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='stadt',
            field=models.CharField(max_length=100, verbose_name='Stadt'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='telefon',
            field=models.CharField(max_length=50, verbose_name='Telefonnummer'),
        ),
    ]
