from django.db import models

# Create your models here.
class Setting(models.Model):
    valuenamechoice= (
     ('TELETOKEN','Telegram Token'),
     ('FSSPTOKEN','FSSP Token'),
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
       
#class Message(models.Model):
class Telegram_session(models.Model):
    update_id    = models.BigIntegerField  ( null='False' )
    message_id   = models.BigIntegerField  ( null='False' )
    message_date = models.DateTimeField   ( auto_now='False', auto_now_add=False)
    message      = models.CharField( max_length=100, null='False', blank='False')  
    user_id      = models.BigIntegerField  ( null='False' )
    chat_id      = models.BigIntegerField  ( null='False' )
    status       = models.BigIntegerField       ( verbose_name='Статус' )
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.id )

class Cookie (models.Model):
    user_id    = models.BigIntegerField  ( null='False' )
    valuename = models.CharField(max_length=1000,null='False', blank='False', verbose_name='Название')
    value       = models.CharField(max_length=1000,null='False', blank='False', verbose_name='Значение')
