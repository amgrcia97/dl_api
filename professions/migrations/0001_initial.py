# Generated by Django 4.0.6 on 2022-07-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Profession')),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Deleted')], default=1, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Profession',
                'verbose_name_plural': 'Professions',
                'db_table': 'professions',
            },
        ),
    ]
