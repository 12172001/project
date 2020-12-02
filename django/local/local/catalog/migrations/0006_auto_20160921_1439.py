from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20160921_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name='D.O.B'),
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(null=True, verbose_name='Died'),
        ),
    ]
