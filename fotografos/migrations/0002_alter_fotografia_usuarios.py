# Generated by Django 5.1.3 on 2024-12-10 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotografos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='usuarios',
            field=models.ManyToManyField(blank=True, null=True, related_name='compartir', to='fotografos.usuario'),
        ),
    ]
