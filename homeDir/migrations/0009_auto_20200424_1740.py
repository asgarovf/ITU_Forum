# Generated by Django 2.1 on 2020-04-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeDir', '0008_auto_20200424_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpost',
            name='tag',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tag - #'),
        ),
    ]
