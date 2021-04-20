from django.db import models


# Create your models here.

class Uploads(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save( self, *args, **kwargs):
        pass
    