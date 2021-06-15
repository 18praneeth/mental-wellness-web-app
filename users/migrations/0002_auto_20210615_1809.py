# Generated by Django 3.2.2 on 2021-06-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='batch',
            new_name='age',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='college_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
    ]
