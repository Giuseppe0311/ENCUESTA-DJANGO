# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alcoholismo(models.Model):
    # Field name made lowercase.
    idalcoholismo = models.CharField(
        db_column='IdAlcoholismo', primary_key=True, max_length=4, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    preg_1 = models.IntegerField(db_column='Preg_1')
    # Field name made lowercase.
    preg_2 = models.IntegerField(db_column='Preg_2')
    # Field name made lowercase.
    preg_3 = models.IntegerField(db_column='Preg_3')
    # Field name made lowercase.
    preg_4 = models.IntegerField(db_column='Preg_4')

    class Meta:
        managed = False
        db_table = 'Alcoholismo'


class Ansiedaddepresion(models.Model):
    # Field name made lowercase.
    idansiedaddepresion = models.CharField(
        db_column='IdAnsiedadDepresion', primary_key=True, max_length=4, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    preg_1 = models.IntegerField(db_column='Preg_1')
    # Field name made lowercase.
    preg_2 = models.IntegerField(db_column='Preg_2')
    # Field name made lowercase.
    preg_3 = models.IntegerField(db_column='Preg_3')
    # Field name made lowercase.
    preg_4 = models.IntegerField(db_column='Preg_4')

    class Meta:
        managed = False
        db_table = 'AnsiedadDepresion'


class Datospersonales(models.Model):
    # Field name made lowercase.
    iddatospersonales = models.CharField(
        db_column='IdDatosPersonales', primary_key=True, max_length=4, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    preg_1 = models.CharField(
        db_column='Preg_1', max_length=64, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    preg_2 = models.CharField(
        db_column='Preg_2', max_length=64, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    preg_3 = models.CharField(
        db_column='Preg_3', max_length=64, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    preg_4 = models.CharField(
        db_column='Preg_4', max_length=64, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    preg_5 = models.CharField(
        db_column='Preg_5', max_length=64, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    preg_6 = models.CharField(
        db_column='Preg_6', max_length=64, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    preg_7 = models.CharField(
        db_column='Preg_7', max_length=64, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    preg_8 = models.CharField(
        db_column='Preg_8', max_length=64, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    dni = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='DNI')

    class Meta:
        managed = False
        db_table = 'DatosPersonales'


class Encuestas(models.Model):
    # Field name made lowercase.
    idencuestas = models.CharField(
        db_column='IdEncuestas', primary_key=True, max_length=4, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    dni = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='DNI')
    # Field name made lowercase.
    idansiedaddepresion = models.ForeignKey(
        Ansiedaddepresion, models.DO_NOTHING, db_column='IdAnsiedadDepresion')
    # Field name made lowercase.
    idpsicosis = models.ForeignKey(
        'Psicosis', models.DO_NOTHING, db_column='IdPsicosis')
    # Field name made lowercase.
    idepilepsia = models.ForeignKey(
        'Epilepsia', models.DO_NOTHING, db_column='IdEpilepsia')
    # Field name made lowercase.
    idalcoholismo = models.ForeignKey(
        Alcoholismo, models.DO_NOTHING, db_column='IdAlcoholismo')

    class Meta:
        managed = False
        db_table = 'Encuestas'


class Epilepsia(models.Model):
    # Field name made lowercase.
    idepilepsia = models.CharField(
        db_column='IdEpilepsia', primary_key=True, max_length=4, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    preg_1 = models.IntegerField(db_column='Preg_1')
    # Field name made lowercase.
    preg_2 = models.IntegerField(db_column='Preg_2')
    # Field name made lowercase.
    preg_3 = models.IntegerField(db_column='Preg_3')
    # Field name made lowercase.
    preg_4 = models.IntegerField(db_column='Preg_4')

    class Meta:
        managed = False
        db_table = 'Epilepsia'


class Perfil(models.Model):
    # Field name made lowercase.
    idperfil = models.CharField(
        db_column='IdPerfil', primary_key=True, max_length=4, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    tipoperfil = models.CharField(
        db_column='TipoPerfil', max_length=20, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'Perfil'


class Psicosis(models.Model):
    # Field name made lowercase.
    idpsicosis = models.CharField(
        db_column='IdPsicosis', primary_key=True, max_length=4, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    preg_1 = models.IntegerField(db_column='Preg_1')
    # Field name made lowercase.
    preg_2 = models.IntegerField(db_column='Preg_2')
    # Field name made lowercase.
    preg_3 = models.IntegerField(db_column='Preg_3')
    # Field name made lowercase.
    preg_4 = models.IntegerField(db_column='Preg_4')

    class Meta:
        managed = False
        db_table = 'Psicosis'


class Usuario(models.Model):
    # Field name made lowercase.
    dni = models.CharField(db_column='DNI', primary_key=True,
                           max_length=8, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    contrasenia = models.CharField(
        db_column='Contrasenia', max_length=30, db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    idperfil = models.ForeignKey(
        Perfil, models.DO_NOTHING, db_column='IdPerfil')

    class Meta:
        managed = False
        db_table = 'Usuario'
