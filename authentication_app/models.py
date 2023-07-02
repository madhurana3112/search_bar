from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, gender, phone_number, password=None):
        if not email:
            raise ValueError("The Email field must be set.")
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, gender, phone_number, password=None):
        user = self.create_user(email, first_name, last_name, gender, phone_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'


class Country(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=52)
    continent = models.CharField(max_length=13, choices=[
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('Africa', 'Africa'),
        ('Oceania', 'Oceania'),
        ('Antarctica', 'Antarctica'),
        ('South America', 'South America')
    ], default='Asia')
    region = models.CharField(max_length=26)
    surface_area = models.FloatField(default=0.00)
    indep_year = models.SmallIntegerField(null=True, blank=True)
    population = models.IntegerField(default=0)
    life_expectancy = models.FloatField(null=True, blank=True)
    gnp = models.FloatField(null=True, blank=True)
    gnpold = models.FloatField(null=True, blank=True)
    local_name = models.CharField(max_length=45)
    government_form = models.CharField(max_length=45)
    head_of_state = models.CharField(max_length=60, null=True, blank=True)
    capital = models.IntegerField(null=True, blank=True)
    code2 = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=35)
    country_code = models.CharField(max_length=3)
    district = models.CharField(max_length=20)
    population = models.IntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CountryLanguage(models.Model):
    CountryCode = models.CharField(max_length=3, default='', primary_key=True)
    Language = models.CharField(max_length=30, default='')
    IsOfficial = models.CharField(max_length=1, choices=(('T', 'T'), ('F', 'F')), default='F')
    Percentage = models.FloatField(default=0.0)

    class Meta:
        db_table = 'countrylanguage'
