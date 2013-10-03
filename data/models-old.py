# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

# Extacted and built by runnig command:
# python manage.py inspectdb --database=dli > data/models.py

from __future__ import unicode_literals

from django.db import models


class Bp(models.Model):    
    user               = models.IntegerField(primary_key=True)
    systolic           = models.IntegerField(null=True, blank=True)
    diastolic          = models.IntegerField(null=True, blank=True)
    measurement        = models.IntegerField(null=True, blank=True)
    measured_on        = models.DateTimeField(null=True, blank=True)
    year               = models.IntegerField(null=True, blank=True)
    month              = models.IntegerField(null=True, blank=True)
    day                = models.IntegerField(null=True, blank=True)
    reporting_category = models.IntegerField(null=True, blank=True)
    timezone           = models.CharField(max_length=8L, blank=True)
    class Meta:
        db_table = 'bp'
        app_label = 'data'

class Glucose(models.Model):
    user               = models.IntegerField(primary_key=True)
    reading            = models.IntegerField(null=True, blank=True)
    glucose            = models.IntegerField(null=True, blank=True)
    glucose_type       = models.IntegerField(null=True, blank=True)
    measurement        = models.IntegerField(null=True, blank=True)
    measured_on        = models.DateTimeField(null=True, blank=True)
    reminded_on        = models.DateTimeField(null=True, blank=True)
    reporting_category = models.IntegerField(null=True, blank=True)
    timezone           = models.CharField(max_length=8L, blank=True)
    class Meta:
        db_table = 'glucose'
        app_label = 'data'

class Init(models.Model):
    user  = models.IntegerField(primary_key=True)
    epoch = models.IntegerField()
    date  = models.DateTimeField()
    class Meta:
        db_table = 'init'
        app_label = 'data'

class Login(models.Model):
    user      = models.IntegerField(primary_key=True)
    login     = models.IntegerField(null=True, blank=True)
    start     = models.DateTimeField(null=True, blank=True)
    year      = models.IntegerField(null=True, blank=True)
    month     = models.IntegerField(null=True, blank=True)
    day       = models.IntegerField(null=True, blank=True)
    dayofweek = models.IntegerField(null=True, blank=True)
    timezone  = models.CharField(max_length=8L, blank=True)
    class Meta:
        db_table = 'login'
        app_label = 'data'

class Pedometer(models.Model):
    user             = models.IntegerField(primary_key=True)
    steps            = models.FloatField(null=True, blank=True)
    walking_calories = models.FloatField(null=True, blank=True)
    walking_distance = models.FloatField(null=True, blank=True)
    walking_time     = models.FloatField(null=True, blank=True)
    running_steps    = models.FloatField(null=True, blank=True)
    running_calories = models.FloatField(null=True, blank=True)
    running_distance = models.FloatField(null=True, blank=True)
    running_time     = models.FloatField(null=True, blank=True)
    other_steps      = models.FloatField(null=True, blank=True)
    other_calories   = models.FloatField(null=True, blank=True)
    other_time       = models.FloatField(null=True, blank=True)
    year             = models.IntegerField(null=True, blank=True)
    month            = models.IntegerField(null=True, blank=True)
    day              = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'pedometer'
        app_label = 'data'

class Questions(models.Model):
    user        = models.IntegerField(primary_key=True)
    question    = models.IntegerField(null=True, blank=True)
    answered_on = models.DateTimeField(null=True, blank=True)
    timezone    = models.CharField(max_length=8L, blank=True)
    class Meta:
        db_table = 'questions'
        app_label = 'data'

class Users(models.Model):
    user                     = models.IntegerField(primary_key=True)
    patient                  = models.IntegerField(null=True, blank=True)
    gender                   = models.CharField(max_length=1L, blank=True)
    dob                      = models.DateField(null=True, blank=True)
    birth_year               = models.IntegerField(null=True, blank=True)
    height                   = models.FloatField(null=True, blank=True)
    weight                   = models.FloatField(null=True, blank=True)
    marital_status           = models.CharField(max_length=16L, blank=True)
    language                 = models.CharField(max_length=24L, blank=True)
    patient_state            = models.CharField(max_length=2L, blank=True)
    country                  = models.CharField(max_length=24L, blank=True)
    patient_deleted          = models.IntegerField(null=True, blank=True)
    patient_created_on       = models.DateTimeField(null=True, blank=True)
    program                  = models.IntegerField(null=True, blank=True)
    program_code             = models.CharField(max_length=16L, blank=True)
    program_deleted          = models.IntegerField(null=True, blank=True)
    program_state            = models.CharField(max_length=2L, blank=True)
    organization             = models.IntegerField(null=True, blank=True)
    organization_name        = models.CharField(max_length=32L, blank=True)
    organization_description = models.CharField(max_length=128L, blank=True)
    organization_active      = models.IntegerField(null=True, blank=True)
    organization_created_on  = models.DateTimeField(null=True, blank=True)
    timezone                 = models.CharField(max_length=8L, blank=True)
    class Meta:
        db_table = 'users'
        app_label = 'data'

class Weight(models.Model):
    user                 = models.IntegerField(primary_key=True)
    height               = models.DecimalField(null=True, max_digits=11, decimal_places=0, blank=True)
    weight               = models.DecimalField(null=True, max_digits=11, decimal_places=0, blank=True)
    bmi                  = models.DecimalField(null=True, max_digits=11, decimal_places=0, blank=True)
    measurement          = models.IntegerField(null=True, blank=True)
    measurement_instance = models.IntegerField(null=True, blank=True)
    measurement_type     = models.IntegerField(null=True, blank=True)
    measured_on          = models.DateTimeField(null=True, blank=True)
    reminded_on          = models.DateTimeField(null=True, blank=True)
    reporting_category   = models.IntegerField(null=True, blank=True)
    timezone             = models.CharField(max_length=8L, blank=True)
    class Meta:
        db_table = 'weight'
        app_label = 'data'

