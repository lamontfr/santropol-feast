# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0026_change_to_emergency_contacts'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='emergencycontact',
            unique_together=set([('client', 'member')]),
        ),
    ]
