# Generated by Django 4.0.6 on 2022-07-18 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_phone_img_accessory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessory',
            old_name='cat',
            new_name='phone',
        ),
    ]