# Generated by Django 4.1.7 on 2023-04-07 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0007_alter_document_file_type_alter_document_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default='ГОСТ', max_length=100),
        ),
    ]
