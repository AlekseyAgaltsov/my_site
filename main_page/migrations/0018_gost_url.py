# Generated by Django 4.1.7 on 2023-04-17 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0017_ansi_api_asme_astm_bs_dd_din_dvs_en_iec_pd_vdi'),
    ]

    operations = [
        migrations.AddField(
            model_name='gost',
            name='url',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main_page.category'),
        ),
    ]