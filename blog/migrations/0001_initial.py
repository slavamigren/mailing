# Generated by Django 4.2.4 on 2023-08-10 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='заголовок')),
                ('text', models.TextField(verbose_name='текст поста')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='аватар')),
                ('created', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
            },
        ),
    ]