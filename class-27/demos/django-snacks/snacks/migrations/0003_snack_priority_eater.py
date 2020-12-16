# Generated by Django 3.1.4 on 2020-12-15 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snacks', '0002_snack_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='priority_eater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]