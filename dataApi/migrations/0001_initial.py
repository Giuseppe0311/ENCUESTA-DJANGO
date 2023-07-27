# Generated by Django 4.2.3 on 2023-07-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alcoholismo',
            fields=[
                ('idalcoholismo', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='IdAlcoholismo', max_length=4, primary_key=True, serialize=False)),
                ('preg_1', models.IntegerField(db_column='Preg_1')),
                ('preg_2', models.IntegerField(db_column='Preg_2')),
                ('preg_3', models.IntegerField(db_column='Preg_3')),
                ('preg_4', models.IntegerField(db_column='Preg_4')),
            ],
            options={
                'db_table': 'Alcoholismo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ansiedaddepresion',
            fields=[
                ('idansiedaddepresion', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='IdAnsiedadDepresion', max_length=4, primary_key=True, serialize=False)),
                ('preg_1', models.IntegerField(db_column='Preg_1')),
                ('preg_2', models.IntegerField(db_column='Preg_2')),
                ('preg_3', models.IntegerField(db_column='Preg_3')),
                ('preg_4', models.IntegerField(db_column='Preg_4')),
            ],
            options={
                'db_table': 'AnsiedadDepresion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Datospersonales',
            fields=[
                ('iddatospersonales', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='IdDatosPersonales', max_length=4, primary_key=True, serialize=False)),
                ('preg_1', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Preg_1', max_length=64)),
                ('preg_2', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Preg_2', max_length=64)),
                ('preg_3', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Preg_3', max_length=64)),
                ('preg_4', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Preg_4', max_length=64)),
                ('preg_5', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Preg_5', max_length=64)),
                ('preg_6', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Preg_6', max_length=64)),
                ('preg_7', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Preg_7', max_length=64)),
                ('preg_8', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Preg_8', max_length=64)),
            ],
            options={
                'db_table': 'DatosPersonales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Encuestas',
            fields=[
                ('idencuestas', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='IdEncuestas', max_length=4, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Encuestas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Epilepsia',
            fields=[
                ('idepilepsia', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='IdEpilepsia', max_length=4, primary_key=True, serialize=False)),
                ('preg_1', models.IntegerField(db_column='Preg_1')),
                ('preg_2', models.IntegerField(db_column='Preg_2')),
                ('preg_3', models.IntegerField(db_column='Preg_3')),
                ('preg_4', models.IntegerField(db_column='Preg_4')),
            ],
            options={
                'db_table': 'Epilepsia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('idperfil', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='IdPerfil', max_length=4, primary_key=True, serialize=False)),
                ('tipoperfil', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='TipoPerfil', max_length=20)),
            ],
            options={
                'db_table': 'Perfil',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Psicosis',
            fields=[
                ('idpsicosis', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='IdPsicosis', max_length=4, primary_key=True, serialize=False)),
                ('preg_1', models.IntegerField(db_column='Preg_1')),
                ('preg_2', models.IntegerField(db_column='Preg_2')),
                ('preg_3', models.IntegerField(db_column='Preg_3')),
                ('preg_4', models.IntegerField(db_column='Preg_4')),
            ],
            options={
                'db_table': 'Psicosis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('dni', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='DNI', max_length=8, primary_key=True, serialize=False)),
                ('contrasenia', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Contrasenia', max_length=30)),
            ],
            options={
                'db_table': 'Usuario',
                'managed': False,
            },
        ),
    ]
