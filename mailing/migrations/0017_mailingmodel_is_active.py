# Generated by Django 4.2.4 on 2023-08-10 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0016_rename_mailing_loglist_mailing_model_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingmodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='активна'),
        ),
    ]
