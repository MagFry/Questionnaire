from django.db import models

# Create your models here.


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name