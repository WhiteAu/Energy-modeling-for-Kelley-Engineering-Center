from django.db import models

class AHU(models.Model): # Represents general AHU readings; no room-specific data.
    spread = models.ForeignKey('Spread_AHU')
    ahu = models.IntegerField()
    read_time = models.TimeField() #date captured in encompassing Spread model
    supply_temp = models.FloatField()
    return_temp = models.FloatField()
    mixed_temp = models.FloatField()
    valve_pct = models.FloatField()
    fan_speed = models.FloatField()
    

class Usage(models.Model): # Steam usage
    spread = models.ForeignKey('Spread_Steam')
    steam = models.IntegerField()
    read_time = models.TimeField()
    

class Reading(models.Model): # a generic data class to represent room information
    room = models.CharField(max_length=50)
    spread = models.ForeignKey('Spread_Room')
    temp = models.FloatField()
    valve = models.FloatField() # heating valve
    flow = models.FloatField() # airflow
    occupied = models.BooleanField()
    class Meta:
        abstract = True #This is our base reading class class
    
    
class Spread(models.Model): # A Spread is a container for multiple AHU's
    #sidechain_ARG = models.OneToManyField(Reading, related_name="reading", null=True)
    pub_date = models.DateField('date polled')
    class Meta:
        abstract = True #This is our base spread class


class Spread_AHU(Spread): # A Spread_AHU is a container for multiple AHU's
    #sidechain_ARG = models.OneToManyField(Reading, related_name="reading", null=True)
    pub_date = models.DateField('date polled')
    
    
class Spread_Steam(Spread): # A Spread_Steam is a container type for multiple steam readings
    #sidechain_ARG = models.OneToManyField(Reading, related_name="reading", null=True)
    pub_date = models.DateField('date polled')
    
    

    
