# Generated by Django 4.2.5 on 2023-10-12 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_post_rider_alter_rider_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rider',
            name='driver',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.driver'),
        ),
    ]