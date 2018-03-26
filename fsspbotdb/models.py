from django.db import models

# Create your models here.
class Setting(models.Model):
    valuenamechoice= (
     ('TELETOKEN','Telegram Token'),
     )
    valuename = models.CharField(
        max_length=100,
        choices=valuenamechoice,
        default='TELETOKEN',
    )
    value=models.CharField(max_length=1000,null='False', blank='False', verbose_name='Значение')
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.valuename)
       
