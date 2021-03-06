from djongo import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=100,default='')
    url = models.CharField(max_length=200,default='')

class Entry(models.Model):
    blog = models.EmbeddedField(
        model_container=Blog
    )
    
    headline = models.CharField(max_length=255)    
    objects = models.DjongoManager()