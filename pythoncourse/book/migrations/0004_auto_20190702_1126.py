# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-07-02 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_completion_suppliment_topiccompletion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='stattypeus',
            new_name='content',
        ),
    ]
