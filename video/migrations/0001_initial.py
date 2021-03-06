# Generated by Django 2.0.5 on 2018-07-14 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filmbase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=150, null=True)),
                ('vid', models.PositiveIntegerField(blank=True, null=True)),
                ('owner_id', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('duration', models.PositiveIntegerField(blank=True, null=True)),
                ('date', models.PositiveIntegerField(blank=True, null=True)),
                ('width', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('height', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('views', models.PositiveIntegerField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('photo', models.CharField(blank=True, max_length=150, null=True)),
                ('first_frame', models.CharField(blank=True, max_length=150, null=True)),
                ('player', models.CharField(blank=True, max_length=250, null=True)),
                ('hd', models.PositiveIntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('kp_id', models.PositiveIntegerField(blank=True, null=True)),
                ('prop_title', models.BooleanField(default=False)),
                ('film', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='filmbase.Film')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='video',
            unique_together={('vid', 'owner_id')},
        ),
    ]
