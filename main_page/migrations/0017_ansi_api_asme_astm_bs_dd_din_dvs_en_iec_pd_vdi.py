# Generated by Django 4.1.7 on 2023-04-11 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0016_iso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ansi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Asme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Astm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Din',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dvs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='En',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Iec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vdi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default='-', max_length=225)),
                ('size', models.IntegerField(default='0', max_length=100)),
                ('file_type', models.CharField(default='pdf', max_length=100)),
            ],
        ),
    ]
