from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model


# Create your models here.
class Skill(models.Model):
    name = models.TextField(max_length=30)
    value = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)

    def __str__(self) -> str:
        return f"{self.name} skill value is {self.value}"


class Education(models.Model):
    university_name = models.TextField()
    start_date = models.PositiveIntegerField()
    end_date = models.PositiveIntegerField(blank=True, null=True)
    is_current = models.BooleanField(blank=True, null=True)
    grade = models.TextField(max_length=30, blank=True, null=True)
    specialization = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)


class Experience(models.Model):
    job_position = models.TextField()
    start_date = models.PositiveIntegerField()
    end_date = models.PositiveIntegerField(blank=True, null=True)
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

User = get_user_model()

class PersonalData(models.Model):
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=30)
    who_i_am = models.TextField(max_length=50, blank=True, null=True)
    summary = models.TextField(max_length=500, blank=True, null=True)
    address = models.TextField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    bday = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    quote = models.TextField(max_length=500, blank=True, null=True)
    quote01 = models.TextField(max_length=500, blank=True, null=True)
    quote02 = models.TextField(max_length=500, blank=True, null=True)
    quote03 = models.TextField(max_length=500, blank=True, null=True)
    quote04 = models.TextField(max_length=500, blank=True, null=True)
    quote05 = models.TextField(max_length=500, blank=True, null=True)
    quote06 = models.TextField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class Contact(models.Model):
    location = models.TextField(max_length=50)
    email = models.TextField(max_length=30)
    phone = models.PositiveBigIntegerField()

class Message(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"You have a text message, subject - {self.subject}"

class PortfolioProject(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media")
    short_description = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    url = models.URLField()