# Generated by Django 2.0.6 on 2018-06-19 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('multigtfs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GTFSForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.CharField(blank=True, max_length=500)),
                ('osm_tag', models.CharField(blank=True, max_length=20)),
                ('gtfs_tag', models.CharField(blank=True, max_length=20)),
                ('frequency', models.IntegerField(blank=True, default=3)),
                ('timestamp', models.DateTimeField(null=True)),
                ('feed', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='multigtfs.Feed')),
            ],
        ),
    ]
