from django.db import models

# Create your models here.


class Ishchi(models.Model):
    ism = models.CharField(max_length=200)
    familliya = models.CharField(max_length=200)
    yili = models.DateField()
    telfon_raqami = models.IntegerField()
   
   
    
    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = 'Ishchi'
        verbose_name_plural = 'Ishchilar'   


