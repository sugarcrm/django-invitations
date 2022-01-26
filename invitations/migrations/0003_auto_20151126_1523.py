# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0002_auto_20151126_0426'),
    ]

    operations = [
        # moved to 0002_auto_20151126_0426
        # migrations.AlterField(
        #     model_name='invitation',
        #     name='inviter',
        #     field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.CASCADE),
        # ),
    ]
