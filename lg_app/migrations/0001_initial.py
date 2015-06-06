# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Complejo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('direccion', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('condicion', models.CharField(default=b'L', max_length=1, choices=[(b'L', b'Local'), (b'V', b'Visitante')])),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('apellido', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('equipo', models.ForeignKey(to='lg_app.Equipo')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('dia', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('cancha', models.ForeignKey(to='lg_app.Cancha')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='turno',
            field=models.ForeignKey(to='lg_app.Turno'),
        ),
        migrations.AddField(
            model_name='cancha',
            name='complejo',
            field=models.ForeignKey(to='lg_app.Complejo'),
        ),
    ]
