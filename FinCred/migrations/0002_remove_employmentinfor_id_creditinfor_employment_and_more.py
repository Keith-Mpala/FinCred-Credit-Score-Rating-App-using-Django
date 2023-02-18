# Generated by Django 4.0.1 on 2022-01-26 20:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FinCred', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employmentinfor',
            name='id',
        ),
        migrations.AddField(
            model_name='creditinfor',
            name='employment',
            field=models.ForeignKey(default='Null', on_delete=django.db.models.deletion.CASCADE, to='FinCred.employmentinfor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employmentinfor',
            name='person',
            field=models.OneToOneField(default='Null', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='FinCred.personaldetails'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
