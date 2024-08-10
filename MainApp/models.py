from django.db import models
from random import sample
import string

# Create your models here.

class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255, unique=True)
    login_password = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(unique=True)
    organization = models.CharField(max_length=255)
    ph_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='media/users')
    super_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Staffs'
        verbose_name = 'Staff'

    def save(self, *args, **kwargs):
        if not self.id:
            while True:
                password = "".join(sample(string.ascii_letters, 6))
                if not self.__class__.objects.filter(login_password=password).exists():
                    self.login_password = password
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name




class Attendance(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Attendances'
        verbose_name = 'Attendance'