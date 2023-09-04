from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class RegisterUser(models.Model):
    email_regex = RegexValidator(regex=r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
                                 message="Email Id must be entered in the format: example326@gmail.com' Up to 50 character allowed.")
    phone_regex = RegexValidator(regex=r'^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$',
                                 message="Phone number must be entered in the format: '999999999',0989279999 Up to 10 digits allowed.")
    Email = models.CharField(validators=[email_regex], max_length=500, null=True)
    Password = models.CharField(max_length=20, null=True)
    Full_Name = models.CharField(max_length=100, null=True)
    Phone = models.CharField(validators=[phone_regex], max_length=15, null=True)
    Address = models.CharField(max_length=500, null=False)
    City = models.CharField(max_length=500, null=False)
    State = models.CharField(max_length=500, null=False)
    Country = models.CharField(max_length=500, null=False)
    Pincode = models.IntegerField(max_length=6,null=True)

    def __str__(self):
        return self.Email

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        if self.pk is None:
            self.created_at = timezone.now()
            usr_name = self.Email
            print(usr_name)
            user_obj = User.objects.create_user(
                username=usr_name, password=self.Password, is_staff=False, email=self.Email,
                
            )
            user_data = list(User.objects.filter(username=user_obj).values('pk'))
            user_data[0].get('pk')
            print(user_data[0].get('pk'))
            self.userId = user_data[0].get('pk')
            self.user_id = user_data[0].get('pk')
            res = super(RegisterUser, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
        else:
            self.updated_at = timezone.now()
            res = super(RegisterUser, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
        return res


class Task(models.Model):
    Title = models.CharField(max_length=30,null=True)
    Body = models.CharField(max_length=300, null=True)
    Summary = models.CharField(max_length=60, null=True)
    Document  = models.FileField(upload_to ='pdf_files/',null=True)
    Categories = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.Title