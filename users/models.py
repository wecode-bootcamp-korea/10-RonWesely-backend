from django.db import models

class Users(models.Model):

    #GENDER_CHOICES= (
    #    ('male', 'Male'),
    #    ('female', 'Female'),
    #)

    userid = models.CharField(max_length=250)
    password = models.CharField(max_length=300)
    phone_no = models.CharField(max_length = 20)
    birthday = models.DateField()
    name = models.CharField(max_length = 10)
    gender = models.CharField(max_length=10)
    on_notification = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add =True)
    modified_at = models.DateTimeField(auto_now = True)

class Meta:
    db_table = "users"

def __str__(self):
    return self.userid












