from django.db import models

# Create your models here.
class Partnership(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    org_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    org_type = models.CharField(max_length=200, default='Other', blank=False)
    primary_goal = models.CharField(max_length=200, default='Default goal', blank=False)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.org_name}"