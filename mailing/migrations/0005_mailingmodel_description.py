# Generated by Django 4.2.4 on 2023-08-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_alter_mailinglist_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingmodel',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание рассылки'),
        ),
    ]
