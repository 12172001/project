from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20160921_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='summary',
        ),
    ]