from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_auto_20161012_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='died'),
        ),
    ]