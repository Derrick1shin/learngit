from django.db import models

# Create your models here.


class UserProfile():
    user_name = models.CharField(unique=True,
                                 null=False,
                                 blank=False,
                                 max_length=15)
    password = models.CharField(null=False,
                                blank=False,
                                max_length=15)

    identity = models.IntegerField(
                                 null=False,
                                 blank=False)


class Food():
    Food_name = models.CharField(unique=True,
                                 null=False,
                                 blank=False,
                                 max_length=15)

    food_id = models.IntegerField(unique=True,
                                 null=False,
                                 blank=False,
                                 max_length=15)

    price = models.IntegerField(unique=True,
                                 null=False,
                                 blank=False,
                                 max_length=15)


class record():
    number = models.IntegerField(unique=True,
                                 null=False,
                                 blank=False,
                                 max_length=15)
    food = models.IntegerField(null=False,
                                 blank=False,
                                 max_length=15)
    date = models.DateTimeField(
                                 null=False,
                                 blank=False,
                                 max_length=15)

