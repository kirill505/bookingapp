from django.db import models
from django.utils import timezone

class Hotel(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.TextField()
    location = models.TextField()
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
