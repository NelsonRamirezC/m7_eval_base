# Generated by Django 5.1.3 on 2024-12-10 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fotografos', '0002_alter_fotografia_usuarios'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fotografia',
            options={'ordering': ['titulo']},
        ),
        migrations.RenameField(
            model_name='fotografia',
            old_name='title',
            new_name='titulo',
        ),
    ]
