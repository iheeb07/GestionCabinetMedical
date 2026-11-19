from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class User (AbstractUser):
    pass

number_validaor=RegexValidator(
    regex=r'^\d{8}$',
    message="le numero doit contenir 8 chiffres"
    )
def birth_date_validator(d):
    if d>= timezone.localdate():
        raise ValidationError("la date de naissance doit etre anterieure a la date actuelle")


class Doctor (User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6), MaxLengthValidator(6)])
    phone=models.CharField(max_length=8, validators=[number_validaor])
    specialities=models.ManyToManyField('AccountAPP.Specialty', related_name='Doctors')

class Patient (User):
    national_id=models.CharField(max_length=8, unique=True, validators=[number_validaor])
    phone=models.CharField(max_length=8, validators=[number_validaor])
    birth_date=models.DateField(validators=[birth_date_validator])

class Specialty(models.Model):
    name=models.CharField(max_length=50, unique=True)
    