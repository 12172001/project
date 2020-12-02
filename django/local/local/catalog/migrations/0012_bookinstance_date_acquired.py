from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20160922_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='date_acquired',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]