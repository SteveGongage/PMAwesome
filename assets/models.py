from django.db import models



# ================================================================
class KeyCabinet(models.Model):
    #client      = models.ForeignKey()
    label       = models.CharField(max_length=20)
    color       = models.CharField(max_length=10, blank=True, null=True)
    max_count   = models.PositiveSmallIntegerField()
    lock_combo  = models.CharField(max_length=10, blank=True, null=True)
    notes       = models.TextField(blank=True, null=True)

    def colorHex(self):
        if (self.color == 'blue'): return '0000AA'
        elif (self.color == 'red'): return 'AA0000'
        else: return '333333'


    def __str__(self):
        return "%s" % self.label

    
# ================================================================
class KeyCabinetSpot(models.Model):
    cabinet     = models.ForeignKey(KeyCabinet)
    number      = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return "%s %s" % (self.cabinet.__str__(), self.number.__str__())

    def save(self, *args, **kwargs):
        if (self.number > self.cabinet.max_count): 
            raise ValueError('Spot number given ('+ self.number +') is higher than available space ('+ self.cabinet.max_count +')')
        else:             
            super(KeyCabinetSpot, self).save(*args, **kwargs)
    
    
# ================================================================
class ReservedKey(models.Model):
    prop                    = models.OneToOneField('properties.Property', primary_key=True, on_delete=models.CASCADE)
    spot                    = models.OneToOneField(KeyCabinetSpot, on_delete=models.CASCADE)
    
    last_update_contact     = models.ForeignKey('messaging.Contact', on_delete=None, blank=True, null=True, limit_choices_to={'isStaff': True})
    last_update_date        = models.DateField()
    location                = models.CharField(max_length=50, blank=True, null=True)
    notes                   = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.prop.__str__()

    class Meta:
        ordering = ['spot__cabinet']
        
# ================================================================
class LockBox(models.Model):
    serial                  = models.CharField(max_length=20, unique=True)    
    prop                    = models.OneToOneField('properties.Property',  on_delete=models.DO_NOTHING, blank=True, null=True)
    last_update_contact     = models.ForeignKey('messaging.Contact', on_delete=models.DO_NOTHING, blank=True, null=True, limit_choices_to={'isStaff': True})
    last_update_date        = models.DateField()
    notes                   = models.TextField(blank=True, null=True)
    combo                   = models.CharField(max_length=10)
    brand                   = models.CharField(max_length=20, blank=True, null=True)
    model                   = models.CharField(max_length=20, blank=True, null=True)
    aquired_date            = models.DateField(blank=True, null=True)
    combo_last_changed_date = models.DateField(blank=True, null=True)
    owner                   = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return self.prop.__str__()

    