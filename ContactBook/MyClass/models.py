from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=64)
    surname =models.CharField(max_length=64)
    description = models.TextField()


class Adress(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house_number = models.SmallIntegerField()
    apartment_number = models.SmallIntegerField()
    person_adress = models.ForeignKey(Person, on_delete=models.CASCADE)


class Phone(models.Model):

    PHONE_TYPE = (
        (1, "domowy"),
        (2, "służbowy"),
        (3, "inny")
    )

    number = models.IntegerField()
    type_number = models.IntegerField(choices=PHONE_TYPE)
    person_phone = models.ForeignKey(Person, on_delete=models.CASCADE)


class Email(models.Model):

    EMAIL_TYPE =(
        (1, "domowy"),
        (2, "służbowy"),
        (3, "inny")
            )
    email = models.CharField(max_length=64)
    email_type = models.IntegerField(choices=EMAIL_TYPE, default=1)
    person_email = models.ForeignKey(Person, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=64)
    person = models.ManyToManyField(Person)
