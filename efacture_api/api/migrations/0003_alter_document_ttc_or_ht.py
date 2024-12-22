# Generated by Django 4.2.17 on 2024-12-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_document_ttc_or_ht'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='ttc_or_ht',
            field=models.CharField(choices=[('TTC', 'TTC'), ('HT', 'HT')], default='NONE', max_length=255),
        ),
    ]
