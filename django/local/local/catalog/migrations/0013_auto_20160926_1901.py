from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_bookinstance_date_acquired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='date_acquired',
            field=models.DateField(default=datetime.date.today),
        ),
    ]