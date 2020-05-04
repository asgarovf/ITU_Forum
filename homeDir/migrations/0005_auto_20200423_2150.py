# Generated by Django 2.1.5 on 2020-04-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeDir', '0004_auto_20200423_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='Resim'),
        ),
        migrations.AlterField(
            model_name='mainpost',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Başlık'),
        ),
    ]
