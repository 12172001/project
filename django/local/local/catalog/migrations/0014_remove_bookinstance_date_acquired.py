from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20160926_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='date_acquired',
        ),
    ]