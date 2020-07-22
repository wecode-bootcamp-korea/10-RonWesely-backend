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
   # survey = models.ManyToManyField(Surveys)

class Meta:
    db_table = "users"

def __str__(self):
    return self.userid

#class Survey(models.Model):
#
#    SURVEY_CHOICES= (
#        ('1', 'off_line'),
#        ('2', 'on_line'),
#        ('3', 'blog'),
#        ('4', 'friends'),
#        ('5', 'etc')
#    )
#
#    choice = models.ChoiceField(("Survey"), max_length=80, choices=SURVEY_CHOICES)
#
#class Meta:
#    db_table = "surveys"
#
#def __str__(self):
#    return self.choice
#
#class Shipping(model.Model):
#    user_id = models.ForeignKeyField(Users, on_delete=models.CASCADE)
#    recipient = models.CharField(max_length=100)
#    phone_no = models.CharField(max_length=50)
#    address = models.CharField(max_length=50)
#    address_detail = models.CharField(max_length=100)
#    requirement = models.CharField(max_length=200)
#    is_default = models.BooleanField(default=False)
#   
#class Meta:
#    db_table = "shippings"
#
#def __str__(self):
#    return self.recipient


