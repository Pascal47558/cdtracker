from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class CD(models.Model):
    band = models.CharField(max_length=64,  blank=True)
    album = models.CharField(max_length=64, blank=True)
    other = models.CharField(max_length=256, blank=True)

    groups = models.ManyToManyField(Group, blank=True, null=True)

    def __str__(self):
        if "".join([group.name for group in self.groups.all()]) != "":
            return self.band + ": " + self.album + " --- " + ", " "".join([group.name for group in self.groups.all()])
        else:
            return self.band + ": " + self.album

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['band', 'album'], 
                name='Duplilcate cd'
            )
        ]