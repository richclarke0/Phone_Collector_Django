# Generated by Django 4.0.6 on 2022-07-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_accessory_accessory_item_alter_accessory_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='accessory',
            options={'ordering': ['-date']},
        ),
    ]
