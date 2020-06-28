# Generated by Django 3.0.7 on 2020-06-28 21:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0004_action_data'),
        ('insiderlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='issuer',
            field=models.ForeignKey(blank=True, help_text='Issuer subject to MAR for delayed disclosure', null=True, on_delete=django.db.models.deletion.CASCADE, to='insiderlist.Issuer', verbose_name='Issuer'),
        ),
        migrations.AddField(
            model_name='action',
            name='obj_created_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='action',
            name='obj_updated_datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='Last updated'),
        ),
        migrations.AlterField(
            model_name='action',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
