from django.db import models
from django.contrib import admin
from django.utils import timezone

class Hotel(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.TextField()
    location = models.CharField(
        max_length = 100,
        choices = (
            ('l01', 'Максимиха'),
            ('l02', 'Горячинск'),
            ('l03', 'Энхалук'),
            ('l03', 'Аршан'),
        ),
        default = 'l01'
    )
    city = models.CharField(
        max_length = 100,
        choices = (
            ('c01', 'Байкал'),
            ('c02', 'Аршан'),
            ('c03', 'Белокурихка'),
        ),
        default = 'c01'
    )
    pre_image = models.FileField()
    price = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
