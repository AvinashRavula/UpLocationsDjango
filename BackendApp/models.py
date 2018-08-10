from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import *


class PriceType(models.Model):
    type = CharField(blank=False, null=False, max_length=20)


class PhoneNumbers(models.Model):
    phone_number = CharField(max_length=12, blank=False, null=False, unique=True)


class EmailIds(models.Model):
    email_id = CharField(max_length=50, blank=False, null=False, unique=True)


class SocialNames(models.Model):
    name = CharField(max_length=50)


class Socials(models.Model):
    social_name = OneToOneField(SocialNames, on_delete=models.CASCADE)
    social_link = CharField(max_length=200, blank=False, null=False)


class SocialContacts(models.Model):
    links = ForeignKey(Socials, on_delete=models.SET_NULL, null=True, blank=True)


class ContactDetails(models.Model):
    phone_numbers = models.ForeignKey(PhoneNumbers, on_delete=models.SET_NULL, null=True, blank=True)
    email_ids = models.ForeignKey(EmailIds, on_delete=models.SET_NULL, null=True, blank=True)
    social_contacts = models.ForeignKey(SocialContacts, on_delete=models.SET_NULL, null=True, blank=True)


class Venues(models.Model):
    venue_name = CharField(blank=False, null=False, max_length=100)
    address = CharField(blank=False, null=False, max_length=500)
    latitude = FloatField(blank=False, null=False)
    longitude = FloatField(blank=False, null=False)
    price_type = models.ForeignKey(PriceType,on_delete=models.SET_NULL, null=True, blank=True)
    contact = models.ForeignKey(ContactDetails, on_delete=models.CASCADE)


class ProfilePicture(models.Model):
    link = CharField(max_length=200, blank=False, null=False, unique=True)


class UserProfiles(models.Model):
    profile_picture = models.ForeignKey(ProfilePicture, models.CASCADE, blank=True, null=True)
    dob = DateField(blank=True, null=True)
    gender = CharField(max_length=6, blank=False, null=False)


class Table(models.Model):
    table_no = IntegerField(max_length=3)
    no_of_seats = IntegerField(max_length=2)
    booked = BooleanField()
    user = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)


class Floor(models.Model):
    venue = models.ForeignKey(Venues, models.CASCADE)
    table = models.ForeignKey(Table, models.CASCADE)
