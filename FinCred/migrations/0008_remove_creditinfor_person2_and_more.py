# Generated by Django 4.0.1 on 2022-01-27 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinCred', '0007_remove_creditinfor_employment_remove_creditinfor_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditinfor',
            name='person2',
        ),
        migrations.RemoveField(
            model_name='employmentinfor',
            name='person',
        ),
        migrations.AddField(
            model_name='creditinfor',
            name='employment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FinCred.employmentinfor'),
        ),
        migrations.AddField(
            model_name='creditinfor',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employmentinfor',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
