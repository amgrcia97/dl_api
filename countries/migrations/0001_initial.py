# Generated by Django 4.0.6 on 2022-07-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Country')),
                ('code', models.CharField(blank=True, max_length=3, null=True, verbose_name='Country Code')),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Deleted')], default=1)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'countries',
            },
        ),
    ]
