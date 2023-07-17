from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Skill(models.Model):
    name = models.TextField(max_length=30)
    value = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)

    def __str__(self) -> str:
        return f"{self.name} skill value is {self.value}"


class Education(models.Model):
    university_name = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    grade = models.TextField(max_length=30, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)


class Experience(models.Model):
    job_position = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField()
    address = models.TextField()
    job_description = models.TextField()
    company_name = models.TextField()


class SocialMedia(models.Model):
    platform_name = models.TextField()
    url = models.URLField()

    def __str__(self) -> str:
        return f"{self.platform_name} account"


class Fact(models.Model):
    name = models.TextField()
    value = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} - {self.value}"


class Service(models.Model):
    service_name = models.TextField()
    service_description = models.TextField()

    def __str__(self) -> str:
        return f"{self.service_name}"


class PersonalData(models.Model):
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=30)
    who_i_am = models.TextField(max_length=50, blank=True, null=True)
    logo = models.TextField(max_length=15, blank=True, null=True)


class Contact(models.Model):
    location = models.TextField(max_length=50)
    email = models.TextField(max_length=30)
    phone = models.PositiveBigIntegerField()
