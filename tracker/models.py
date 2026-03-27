from django.db import models

# Create your models here.
class CD(models.Model):
    band = models.CharField(max_length=128)
    album = models.CharField(max_length=128)
    #other = models.CharField(max_length=512, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['band', 'album'], 
                name='Duplilcate cd'
            )
        ]