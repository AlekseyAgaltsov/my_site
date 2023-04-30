# Generated by Django 4.1.7 on 2023-04-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0015_category_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
    ]