from django.db import models

# Create your models here.
class CD(models.Model):
    band = models.CharField(max_length=64,  blank=True)
    album = models.CharField(max_length=64, blank=True)
    other = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.band + ": " + self.album

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['band', 'album'], 
                name='Duplilcate cd'
            )
        ]