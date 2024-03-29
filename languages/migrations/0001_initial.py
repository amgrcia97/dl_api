# Generated by Django 4.1.6 on 2023-02-07 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Language')),
                ('code', models.SlugField(unique=True, verbose_name='Code')),
                ('status', models.BooleanField(default=True, verbose_name='Active?')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'db_table': 'languages',
            },
        ),
        migrations.CreateModel(
            name='CountryLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=3, null=True, unique=True, verbose_name='Country Language Code')),
                ('status', models.BooleanField(default=True, verbose_name='Active?')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_language', to='addresses.country')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_language_language', to='languages.language')),
            ],
            options={
                'verbose_name': 'Country Language',
                'verbose_name_plural': 'Countries Language',
                'db_table': 'countries_language',
            },
        ),
    ]
