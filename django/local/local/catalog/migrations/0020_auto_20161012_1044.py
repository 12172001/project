from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]