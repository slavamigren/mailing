# Generated by Django 4.2.4 on 2023-08-03 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя клиента')),
                ('mail', models.EmailField(max_length=50, verbose_name='email клиента')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LogList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='время ошибки')),
                ('error_type', models.CharField(max_length=50, verbose_name='тип ошибки')),
                ('error_message', models.TextField(verbose_name='сообщение об ошибке')),
            ],
            options={
                'verbose_name': 'ошибка',
                'verbose_name_plural': 'ошибки',
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='MailingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='название рассылки')),
                ('time_from', models.TimeField(verbose_name='начало рассылки')),
                ('time_to', models.TimeField(verbose_name='окончание рассылки')),
                ('week_day', models.SmallIntegerField(blank=True, null=True, verbose_name='день недели')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
                'ordering': ['time_from'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('message', models.TextField(verbose_name='сообщение')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.client', verbose_name='клиент')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingmodel', verbose_name='рассылка')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.message', verbose_name='сообщение')),
            ],
            options={
                'verbose_name': 'письмо',
                'verbose_name_plural': 'письма',
            },
        ),
    ]