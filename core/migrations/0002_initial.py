# Generated by Django 4.2.5 on 2023-10-12 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='rider',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.rider'),
        ),
        migrations.AddField(
            model_name='driver',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
    ]