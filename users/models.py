from django.db import models

class User(models.Model):
    email        = models.CharField(max_length=250)
    password     = models.CharField(max_length=300)
    phone_number = models.CharField(max_length = 20)
    birthday     = models.DateField()
    name         = models.CharField(max_length = 10)
    gender_type  = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)
    is_notified  = models.BooleanField(default = False)
    created_at   = models.DateTimeField(auto_now_add =True)
    modified_at  = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "users"


class Gender(models.Model):
    name = models.CharField(max_length=10)

    class Meta: 
        db_table = "genders"


class Path(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "paths"


class Path_result(models.Model):
    user       = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    path_lists = models.ForeignKey('Path', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "path_results"


class Shipping(models.Model):
    user           = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    recipient      = models.CharField(max_length=10)
    phone_number   = models.CharField(max_length=20)
    address        = models.CharField(max_length=20)
    address_detail = models.CharField(max_length=100)
    requirement    = models.CharField(max_length=100)
    is_default     = models.BooleanField()

    class Meta:
        db_table = "shippings"

