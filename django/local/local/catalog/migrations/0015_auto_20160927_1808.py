from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_remove_bookinstance_date_acquired'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='subject_name',
        ),
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.CharField(default='Fantasy', help_text='Enter a book category - e.g. Science Fiction, French Poetry etc.', max_length=200),
            preserve_default=False,
        ),
    ]