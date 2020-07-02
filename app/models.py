from django.db import models

# Create your models here.

class activité(models.Model):
    date = models.DateField()
    titre = models.TextField()
    contenue = models.TextField()
    image = models.ImageField(upload_to='imgs', null=True)
    def __str__(self):
        return self.titre