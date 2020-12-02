from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20160921_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Enter a brief description of the book', max_length=1000),
        ),
    ]