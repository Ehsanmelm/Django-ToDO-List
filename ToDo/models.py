from django.db import models

# Create your models here.


class challenge_list_Model(models.Model):
    challenge = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.challenge}"
