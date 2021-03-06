# Generated by Django 2.0.5 on 2018-07-13 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmbase', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film_List_Elem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('order', models.IntegerField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='filmbase.Film')),
                ('owner_list', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.List')),
            ],
        ),
    ]
