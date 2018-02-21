# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-21 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgmgm', '0018_auto_20180221_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(verbose_name='Beschreibung'),
        ),
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
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email Adresse'),
        ),
        migrations.AlterField(
            model_name='kontakt',
            name='nachname',
            field=models.CharField(max_length=100, verbose_name='Nachname'),
        ),
        migrations.AlterField(
            model_name='kontakt',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgmgm.Organisation'),
        ),
        migrations.AlterField(
            model_name='kontakt',
            name='rolle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Rolle'),
        ),
        migrations.AlterField(
            model_name='kontakt',
            name='telefon',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Telfonnummer'),
        ),
        migrations.AlterField(
            model_name='kontakt',
            name='vorname',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Vorname'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='bundesland',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgmgm.Bundesland'),
        ),
    ]
