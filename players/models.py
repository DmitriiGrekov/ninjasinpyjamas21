from django.db import models

class Players(models.Model):
    name = models.CharField(max_length=120)
    shortdescription = models.TextField(max_length=120)
    description = models.TextField()
    mainimg = models.TextField()
    img1 = models.TextField()
    img2 = models.TextField()
    img3 = models.TextField()
    img4 = models.TextField()
    img5 = models.TextField()
    img6 = models.TextField()
    videp = models.TextField()


    def __str__(self):
        return self.name
