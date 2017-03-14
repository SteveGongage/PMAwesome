
import localflavor.us.models
import datetime, math
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.db import models
#from messaging.models import Contact, Message



# ================================================================
class Property(models.Model):

    name 			= models.CharField(max_length=50)
    slug            = models.CharField(max_length=100)

    # Location of the Property
    addressNumeric	= models.PositiveIntegerField(verbose_name='Street Numeric', help_text='Number only')
    addressStreet	= models.CharField(max_length=30, verbose_name='Street Name', help_text='Street name only, no numeric, no unit number.')
    addressUnit		= models.CharField(max_length=20, blank=True, verbose_name='Unit')
    addressCity		= models.CharField(max_length=20, verbose_name='City')
    addressState	= localflavor.us.models.USStateField(default='FL', verbose_name='State')
    addressZipcode	= localflavor.us.models.USZipCodeField(verbose_name='Zip Code')
    addressCounty	= models.CharField(max_length=20, verbose_name='County')
    
    addressFull		= models.CharField(max_length=100)
    addressShort    = models.CharField(max_length=50)    
    #addressStreet1	= models.CharField(max_length=50, blank=True)	# May not be necessary
    #addressStreet2	= models.CharField(max_length=50, blank=True)	# May not be necessary

    neighborhood	= models.CharField(max_length=30, blank=True)
    partOfTown		= models.CharField(max_length=30, blank=True, verbose_name='Part of Town')

    #mapping info
    isMapable		= models.BooleanField(default=False)
    mapNotes		= models.TextField(blank=True)
    mapLatitude		= models.FloatField(null=True, blank=True)
    mapLongitude	= models.FloatField(null=True, blank=True)

    # Features of the Property

    PROPERTY_TYPE_SINGLEFAMILY	= 'sfhouse'
    PROPERTY_TYPE_CONDO			= 'condo'
    PROPERTY_TYPE_TOWNHOUSE		= 'townhouse'
    PROPERTY_TYPE_COMMERCIAL	= 'commercial'
    PROPERTY_TYPE_CHOICES=(
        (PROPERTY_TYPE_SINGLEFAMILY, 'House'),
        (PROPERTY_TYPE_CONDO, 'Condo'),
        (PROPERTY_TYPE_TOWNHOUSE, 'Townhouse'),
        (PROPERTY_TYPE_COMMERCIAL, 'Commercial'),
    )

    propertyType    = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default=PROPERTY_TYPE_SINGLEFAMILY, verbose_name='Type of Property')
    areaHeatedSqFt	= models.PositiveIntegerField(null=True, blank=True, verbose_name='Heated Area')
    areaLotSqFt		= models.PositiveIntegerField(null=True, blank=True, verbose_name='Lot Area')
    bedrooms		= models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Bedrooms' )
    bathroomsFull	= models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Full Bathrooms')
    bathroomsHalf	= models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Half Bathrooms')
    yearBuilt		= models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Year Built')

    petCatsOK       = models.BooleanField(default=True, verbose_name='Cats OK?')
    petDogsOK       = models.BooleanField(default=True, verbose_name='Dogs OK?')
    petRestrictions = models.CharField(max_length=100, blank=True, null=True, verbose_name='Pet Restrictions')

    marketingDescription = models.TextField(null=True, blank=True, verbose_name='Marketing Description')

    dateContractStart = models.DateField(blank=True, null=True, verbose_name='Contract Start Date')
    contactManager  = models.ForeignKey('messaging.Contact', on_delete=models.CASCADE, blank=True, null=True, limit_choices_to={'isStaff': True}, verbose_name='Property Manager')

    ext_appfolioID  = models.CharField(max_length=40, blank=True, null=True, verbose_name='Appfolio ID')
    ext_MLSID       = models.CharField(max_length=20, blank=True, null=True, verbose_name='MLS ID')


    HOA_name             = models.CharField(max_length=50, blank=True, null=True, verbose_name='HOA Name')
    HOA_email            = models.EmailField(blank=True, null=True, verbose_name='HOA Email')
    HOA_phone            = localflavor.us.models.PhoneNumberField(blank=True, null=True, verbose_name='HOA Phone')

    HOA_approvesTenants  = models.BooleanField(default=False, verbose_name='HOA Approves Tenants')
    HOA_gateCode         = models.CharField(max_length=20, blank=True, null=True, verbose_name='Gate Code')

    system_isWellWater              = models.BooleanField(default=False, verbose_name='On Well Water?')    
    system_isSeptic                 = models.BooleanField(default=False, verbose_name='On Septic?')
    system_mainWaterShutoff         = models.CharField(max_length=20, blank=True, null=True, verbose_name='Main Water Shut Off')    
    system_refrigeratorWaterShutoff = models.CharField(max_length=20, blank=True, null=True, verbose_name='Refrigerator Water Shut Off')    
    system_excludedItems            = models.CharField(max_length=100, blank=True, null=True, verbose_name='Excluded Items', help_text='List the areas or items in the home that are excluded from tenant use')
    system_irrigationController     = models.CharField(max_length=20, blank=True, null=True, verbose_name='Irrigation Controller')
    system_irrigationSchedule       = models.CharField(max_length=40, blank=True, null=True, verbose_name='Irrigation Schedule')


    POOL_NONE		= 'none'
    POOL_PRIVATE	= 'private'
    POOL_COMMUNITY	= 'community'
    POOL_BOTH		= 'both'
    POOL_CHOICES	= (
        (POOL_NONE, 'None'), 
        (POOL_PRIVATE, 'Private'),
        (POOL_COMMUNITY, 'Community'),
        (POOL_BOTH, 'Both'),
    )
    poolType		= models.CharField(max_length=10, choices=POOL_CHOICES, default=POOL_NONE, verbose_name='Pool Type')


    archived_on		= models.DateTimeField(blank=True, null=True, verbose_name='Archive On')

    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
   
    def hasPool(self):
        return self.poolType != self.POOL_NONE

    def bathrooms(self):
        return self.bathroomsFull.__str__() +'.'+ self.bathroomsHalf.__str__()

    def currentLease(self):
        today = datetime.date.today()
        leases = self.lease_set.filter(dateLeaseStart__lte=today, dateLeaseEnd__gte=today)
        if (len(leases) > 0):
            return leases[0]

    def futureLease(self):
        today = datetime.date.today()
        leases = self.lease_set.filter(dateLeaseStart__gte=today).order_by('dateLeaseStart')
        if (len(leases) > 0):
            return leases[0]

    def previousLease(self):
        today = datetime.date.today()
        leases = self.lease_set.filter(dateLeaseEnd__lte=today).order_by('-dateLeaseEnd')
        if (len(leases) > 0):
            return leases[0]

    def daysVacant(self):
        dv = 0
        today = datetime.date.today()

        if (self.currentLease() != None):
            dv = 0
        elif (self.previousLease() != None):
            diff = self.previousLease().dateLeaseEnd
            dv = diff.days
        else:
            dv = (today - self.dateContractStart).days
        return dv
    
    def daysTillMoveIn(self):
        if (self.futureLease() != None):
            today = datetime.date.today()
            return (self.futureLease().dateLeaseStart - today).days

    def daysBetweenLeases(self):
        if (self.futureLease() != None):
            d1 = None
            d2 = None
            if (self.previousLease() != None):
                d1 = self.previousLease().dateLeaseEnd
            elif (self.currentLease() != None):
                d1 = self.currentLease().dateLeaseEnd
            else:
                d1 = self.dateContractStart

            if (d1 != None):
                d2 = self.futureLease().dateLeaseStart
                if (d2 != None):
                    return (d2 - d1).days

    def percentBetweenLeases(self):
        if (self.daysVacant() and self.daysBetweenLeases()):
            return round(self.daysVacant() / self.daysBetweenLeases() * 100)
        else:
            return 0

    def addLog(self, notes):
        self.addActivity(
            notes = notes,
            priority = PropertyActivity.PRIORITY_LOG,
            type = PropertyActivity.TYPE_INFO
        )
        # newActivity = PropertyActivity(
        #     prop            = self,
        #     notes           = notes, 
        #     priority        = PropertyActivity.PRIORITY_LOG,
        #     type            = PropertyActivity.TYPE_INFO,
        #     activity_on     = timezone.datetime.now(),
        #     alertStart_on   = datetime.date.today(),
        #     )
        # newActivity.save()

    def addActivity(self, notes="", priority='low', type='info', activity_on = timezone.datetime.now(), alertStart_on   = datetime.date.today()):
        newActivity = PropertyActivity(
            prop            = self,
            notes           = notes, 
            priority        = priority,
            type            = type,
            activity_on     = activity_on,
            alertStart_on   = alertStart_on,
            )
        newActivity.save()


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Properties'
        ordering = ["name"]

    def save(self, *args, **kwargs):
        # rebuild address short strings
        self.addressShort = self.addressNumeric.__str__() +' '+ self.addressStreet
        self.name = self.addressStreet +' '+ self.addressNumeric.__str__()
        if (self.addressUnit.strip() != ''):
            self.addressShort += ', '+ self.addressUnit
            self.name += ' '+ self.addressUnit
        
        self.addressFull = self.addressShort +', '+ self.addressCity +', '+ self.addressState +', '+ self.addressZipcode
        self.slug = slugify(self.addressFull)
        
        super(Property, self).save(*args, **kwargs)

        # log the creation of the property
        self.addLog('Property saved')


# ================================================================
class Asset(models.Model):
    property 	= models.ForeignKey(Property, on_delete=models.CASCADE)

    label		= models.CharField(max_length=30)
    assetType	= models.CharField(max_length=20, choices=(('appliance', 'Appliance'),('system', 'System')))
    color		= models.CharField(max_length=30, blank=True, null=True)
    brand		= models.CharField(max_length=20, blank=True, null=True)
    model		= models.CharField(max_length=20, blank=True, null=True)
    serial		= models.CharField(max_length=20, blank=True, null=True)
    location	= models.CharField(max_length=50, blank=True, null=True)
    notes		= models.TextField(blank=True, null=True)
    yearAquired	= models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering=('label',)

# ================================================================
class VendorService(models.Model):
    prop    		= models.ForeignKey(Property, on_delete=models.CASCADE)
    
    label			= models.CharField(max_length=20)
    companyName		= models.CharField(max_length=40, blank=True)
    contactName		= models.CharField(max_length=50, blank=True)
    phone1			= models.CharField(max_length=16, blank=True)
    phone2			= models.CharField(max_length=16, blank=True)
    email			= models.CharField(max_length=50, blank=True)
    address			= models.CharField(max_length=100, blank=True)
    accountNumber	= models.CharField(max_length=40, blank=True)
    notes			= models.TextField(blank=True)

    def __str__(self):
        return self.label +': '+ self.companyName

    class Meta:
        ordering=('label',)

# ================================================================
class AccessDevice(models.Model):
    prop    		= models.ForeignKey(Property, on_delete=models.CASCADE)

    label			= models.CharField(max_length=20)
    ownerCount		= models.PositiveSmallIntegerField(blank=True)
    notes			= models.TextField(blank=True)
    
    def __str__(self):
        return self.label

    class Meta:
        ordering=('label',)

# ================================================================
class FeatureOption(models.Model):
    label			= models.CharField(max_length=20)
    groupMain		= models.CharField(max_length=20, choices=(('community', 'Community'), ('included', 'Included'), ('exterior', 'Exterior'), ('interior', 'Interior'), ))
    groupSub		= models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering=('groupMain', 'groupSub', 'label')



# ================================================================
class Feature(models.Model):
    prop    		= models.ForeignKey(Property, on_delete=models.CASCADE)
    featureOption	= models.ForeignKey(FeatureOption, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.property.name +' '+ self.featureOption.label

# ================================================================
class Lease(models.Model):
    prop		= models.ForeignKey(Property, on_delete= models.DO_NOTHING)

    isActive                = models.BooleanField(default=True)
    dateLeaseStart       	= models.DateField()
    dateLeaseEnd  	        = models.DateField()

    # Fees
    terms_priceRent			= models.PositiveIntegerField()
    terms_depositSecurity   = models.PositiveIntegerField()
    terms_lateGraceDays		= models.PositiveSmallIntegerField(default=3)
    terms_feeLate			= models.PositiveIntegerField(default=100)
    terms_feeLateNotice	    = models.PositiveIntegerField(default=25)
    # terms_depositPet 		= models.IntegerField(blank=True, null=True)
    # terms_feePet			= models.IntegerField(default=0)
    # terms_feeCleaning		= models.IntegerField()
    # terms_feeCarpet		= models.IntegerField()
    # terms_feeRenewal      = models.IntegerField(default=0)


    # Start of Lease Transition Information
    start_dateLeaseSigned	=models.DateField(blank=True, null=True)
    start_isRenewal         =models.BooleanField(default=False)
    start_dateMoveIn        =models.DateField(blank     =True, null=True)
    start_moveInNotes       =models.TextField(blank     =True, null=True) 

    # End of Lease Transition Information  
    end_dateMoveOut    	    =models.DateField(blank     =True, null=True)
    end_actionNotes 	    =models.TextField(blank     =True, null=True)
    end_moveOutNotes   	    =models.TextField(blank     =True, null=True)
    
    # End Actions: at the end of the lease term, owners and tenants have to decide what will happen before the end of the lease...
    ACTION_UNDECIDED        ='undecided'
    ACTION_NEWTENANT        ='new tenant'
    ACTION_RENEW		    ='current tenant'
    ACTION_RETURNTOOWNER    ='return to owner'
    ACTION_SALE             ='for sale'
    ACTION_MONTHTOMONTH     ='month to month'
    ACTION_CHOICES=(
        (ACTION_UNDECIDED, 		'Undecided'),
        (ACTION_NEWTENANT, 		'Find New Tenant'),
        (ACTION_RENEW, 			'Keep Current Tenant'),
        (ACTION_RETURNTOOWNER, 	'Return to Owner'),
        (ACTION_SALE, 			'List for Sale'),
        (ACTION_MONTHTOMONTH, 	'Month to Month'),
    )
    end_ActionTenants 	   	= models.CharField(max_length=30, choices=ACTION_CHOICES, default="undecided")
    end_ActionTenantsDate 	= models.DateTimeField(blank =True, null =True)
    end_ActionOwner 		= models.CharField(max_length=30, choices=ACTION_CHOICES, default="undecided")
    end_ActionOwnerDate  	= models.DateTimeField(blank =True, null =True)
    end_ActionFinal 		= models.CharField(max_length=30, choices=ACTION_CHOICES, default="undecided")
    end_ActionFinalDate   	= models.DateTimeField(blank =True, null =True)

    #pets
    pet1=models.CharField(max_length=30, blank=True, null=True)
    pet2=models.CharField(max_length=30, blank=True, null=True)
    pet3=models.CharField(max_length=30, blank=True, null=True)
    pet4=models.CharField(max_length=30, blank=True, null=True)
    pet5=models.CharField(max_length=30, blank=True, null=True)

    def isFuture(self):
        return self.dateLeaseStart > datetime.date.today()

    def isCurrent(self):
        return self.dateLeaseStart <= datetime.date.today() and self.dateLeaseEnd >= datetime.date.today()

    def isPast(self):
        return self.dateLeaseEnd < datetime.date.today()

    def status(self):
        '''Returns "future", "current", or "past" depending on the dates of the lease. '''
        if (self.isFuture()):
            return 'future'
        elif (self.isCurrent()):
            return 'current'
        else:
            return 'past'

    def daysInLease(self):
        diff = self.dateLeaseEnd - self.dateLeaseStart
        return diff.days
    
    def monthsInLease(self):
        diff = self.dateLeaseEnd - self.dateLeaseStart
        return round(diff.days / 30) 
    
    def daysUsed(self):
        diff = datetime.date.today() - self.dateLeaseStart
        return diff.days        

    def daysRemaining(self):
        if (self.isPast()):
            return 0
        elif (self.isFuture()):
            return self.daysInLease()
        else: 
            diff = self.dateLeaseEnd - datetime.date.today()
            return diff.days if (diff.days > 0) else 0
    
    def percentUsed(self):
        ratio = 0        
        if (self.daysUsed() > 0):
            ratio = self.daysUsed() / self.daysInLease() * 100 
        return round(ratio, 2)
        
    def __str__(self):
        #return self.property.__str__() +': '+ self.dateLeaseStart.__str__()
        return self.prop.__str__() +' - '+ self.dateLeaseStart.__str__()

    def Meta():
        ordering = ['-dateLeaseStart']

    def save(self, *args, **kwargs):
        saveLog = False

            
        

        if self.pk is None and self.start_dateLeaseSigned is not None:
            saveLog = True
        elif self.pk is not None:
            
        
            self.prop.addActivity(
                notes       = 'New Lease Signed: '+ self.__str__(), 
                priority    = PropertyActivity.PRIORITY_INFO, 
                type        = PropertyActivity.TYPE_LEASE_SIGNED,
                activity_on = self.start_dateLeaseSigned
                )
        super(Lease, self).save(*args, **kwargs) 


     
# ================================================================
class Fee(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(blank=True, null=True)
    defaultAmount=models.PositiveIntegerField(default=0)
    
    TYPE_RENT='rent'             # collected and paid to home owner
    TYPE_FEE_TENANT='tenant fee' # collected and kept by PM    
    TYPE_FEE_OWNER='owner fee'   # collected and kept by PM    
    TYPE_DEPOSIT='deposit'       # collected to be held in escrow and partially / fully returned
    TYPE_SERVICE='service'       # collected to be paid to 3rd party service provider (pool, lawn, etc)
    type=models.CharField(max_length=20, choices=(
        (TYPE_RENT, 'Rent'),
        (TYPE_FEE_OWNER, 'Owner Fee'),
        (TYPE_FEE_TENANT, 'Tenant Fee'),
        (TYPE_DEPOSIT, 'Deposit'),
        (TYPE_SERVICE, 'Service'),
    ))

    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)
    archived_on=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def Meta():
        ordering = ['name']

# ================================================================
class LeaseFee(models.Model):
    lease=models.ForeignKey(Lease, on_delete=models.CASCADE)
    fee=models.ForeignKey(Fee, on_delete=models.CASCADE)
    amount=models.IntegerField()


# ================================================================
class LeaseContact(models.Model):
    lease		= models.ForeignKey(Lease, on_delete= models.CASCADE)
    contact		= models.ForeignKey('messaging.Contact', on_delete=models.DO_NOTHING)
    TYPE_TENANT 		= 'tenant'
    TYPE_COSIGNER 		= 'cosigner'
    TYPE_TENANT_AGENT 	= 'tenant agent'
    TYPE_OWNER 			= 'owner'
    TYPE_OTHER 			= 'other'
    TYPE_CHOICES=(
        (TYPE_TENANT,       'Tenant'),
        (TYPE_COSIGNER,     'Co-signer'),
        (TYPE_TENANT_AGENT, 'Tenant\'s Agent'),
        (TYPE_OWNER,        'Owner'),
        (TYPE_OTHER,        'Other'),
    )
    type=models.CharField(max_length=20, choices=TYPE_CHOICES)

    notes       = models.TextField(blank=True, null=True)
    doNotRenew  = models.BooleanField(default=False)
    certifiedFundsOnly = models.BooleanField(default=False)

    
    isUnderage=models.BooleanField(default=False)
    isFinanciallyResponsible=models.BooleanField(default=False)

    def nameFull(self):
        return self.contact.nameFull()

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.lease.prop.addLog('Added a new Contact to the Lease: '+ self.contact.nameFull() +' - '+ self.lease.__str__())

        super(LeaseContact, self).save(*args, **kwargs)




# ================================================================
class PropertyOwner(models.Model):
    prop		= models.ForeignKey(Property, on_delete= models.CASCADE)
    contact		= models.ForeignKey('messaging.Contact', on_delete=models.CASCADE, limit_choices_to={'isOwner': True})

    TYPE_OWNER 		= 'owner'
    TYPE_AUTHORIZED	= 'authorized contact'
    TYPE_AGENT  	= 'agent'
    TYPE_LAWYER 	= 'lawyer'
    TYPE_OTHER 		= 'other'
    TYPE_CHOICES=(
        (TYPE_OWNER,    'Owner'),
        (TYPE_AUTHORIZED,'Contact'),
        (TYPE_AGENT,    'Sales Agent'),
        (TYPE_LAWYER,   'Lawyer'),
        (TYPE_OTHER,    'Other'),
    )
    type=models.CharField(max_length=20, choices=TYPE_CHOICES)
    
    isForeignOwner  = models.BooleanField(default=False)
     

    percentageShare = models.PositiveSmallIntegerField(default=100)
    holdPayments    = models.BooleanField(default=False)
    sendEmailNotifications = models.BooleanField(default=True)

    notes       = models.TextField(blank=True, null=True)

    active_on   = models.DateField(auto_now_add=True)
    archive_on  = models.DateField(blank=True, null=True)

    
    def nameFull(self):
        return self.contact.nameFull()

    def typeDescription(self):
        desc = 'Owner'
        if (self.type != 'owner'):
            desc = 'Owner\'s '+ self.get_type_display()
        
        return desc

    def __str__(self):
        return self.contact.nameFull()
        
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.prop.addLog('Added a new Property Owner: '+ self.contact.nameFull())

        super(PropertyOwner, self).save(*args, **kwargs)



# ================================================================
class PropertyActivity(models.Model):
    prop                = models.ForeignKey(Property, on_delete=models.CASCADE)
    createdByContact    = models.ForeignKey('messaging.Contact', on_delete=None, blank=True, null=True, limit_choices_to={'isStaff': True})
    message             = models.ForeignKey('messaging.Message', on_delete=None, blank=True, null=True, limit_choices_to={'created_on__gte': datetime.datetime.now() - datetime.timedelta(days=(7))})

    
    

    

    activity_on     = models.DateTimeField()                                # date the activity takes place.
    resolved_on     = models.DateTimeField(blank=True, null=True)           # date the activity is marked as resolved

    notes           = models.TextField(blank=True, null=True)


    isAlert         = models.BooleanField(default=True)
    alertStart_on   = models.DateField()                                    # when should this alert be visible?
    alertEnd_on     = models.DateField(blank=True, null=True)               # when should this alert be muted?  Can be blank to be user muted.

    created_on      = models.DateTimeField(auto_now_add=True)               # date this was created.  System use only

  

    PRIORITY_URGENT = 100       
    PRIORITY_HIGH	= 80       
    PRIORITY_MEDIUM	= 60        
    PRIORITY_LOW	= 40        
    PRIORITY_INFO   = 20        
    PRIORITY_LOG    = 10       
    UI_PRIORITY = {
        PRIORITY_URGENT: {    # urgent            Immediate attention - undismissable alert banner in system
            'DISPLAY':      'Urgent',
            'STYLE':        'urgent pulse',
            'FA_ICON':      'fa fa-exclamation-triangle'
        },
        PRIORITY_HIGH: {     # high              Immediate attention - dismissable popup alert
            'DISPLAY':      'High',
            'STYLE':        'danger',
            'FA_ICON':      'fa fa-arrow-circle-up'
        },
        PRIORITY_MEDIUM: {     # normal - default  Attention needed    - dismissable popup alert
            'DISPLAY':      'Normal',
            'STYLE':        'warning',
            'FA_ICON':      'fa fa-arrow-circle-right'
        },
        PRIORITY_LOW: {     # low               Attention needed    - short term popup alert
            'DISPLAY':      'Low',
            'STYLE':        'success',
            'FA_ICON':      'fa fa-arrow-circle-down'
        },
        PRIORITY_INFO: {     # info              Shows up in reports - no popup alert
            'DISPLAY':      'Info',
            'STYLE':        'info',
            'FA_ICON':      'fa fa-info-circle'
        },
        PRIORITY_LOG: {     # System Log        Shows up in reports - no popup alert
            'DISPLAY':      'Log',
            'STYLE':        'muted',
            'FA_ICON':      'fa fa-info'
        },
    }
    
    priority = models.PositiveSmallIntegerField(default=PRIORITY_MEDIUM, choices=(
        (PRIORITY_URGENT,   UI_PRIORITY[PRIORITY_URGENT]['DISPLAY']),
        (PRIORITY_HIGH,     UI_PRIORITY[PRIORITY_HIGH]['DISPLAY']),
        (PRIORITY_MEDIUM,   UI_PRIORITY[PRIORITY_MEDIUM]['DISPLAY']),
        (PRIORITY_LOW,      UI_PRIORITY[PRIORITY_LOW]['DISPLAY']),
        (PRIORITY_INFO,     UI_PRIORITY[PRIORITY_INFO]['DISPLAY']),
        (PRIORITY_LOG,      UI_PRIORITY[PRIORITY_LOG]['DISPLAY']),
    ))
 
    TYPE_LEASE_EXPIRING  = "lease expiring"
    TYPE_LEASE_SIGNED    = "lease signed"      
    TYPE_MOVING_OUT      = "moving out"          
    TYPE_MOVING_IN       = "moving in"          
    TYPE_SERVICE_REQUEST = "service request"     
    TYPE_WORK_ORDER      = "work order"              
    TYPE_VACANT          = "vacant"              
    TYPE_TENANTS_NEEDED  = "tenants needed"      
    TYPE_INCIDENT        = "incident"            
    TYPE_RENT_LATE       = "rent late"           
    TYPE_EVICTION        = "eviction"            
    TYPE_OFFICIAL_NOTICE = "official notice"            
    TYPE_VIOLATION       = "violation"            
    TYPE_TENANT          = "tenant"              
    TYPE_OWNER           = "owner"               
    TYPE_INFO_INCOMPLETE = "info incomplete"     
    TYPE_INFO            = "info"            
    TYPE_RENT_PAID       = "rent paid"           
    TYPE_INSPECTION      = "inspection"          
    TYPE_SERVICE         = "service"             

    UI_TYPE = {
        TYPE_LEASE_EXPIRING:      {
            "DISPLAY":          "Lease Expiring",
            "VERBOSE":          "Lease expiring in the near future",
            "FA_ICON":          "fa fa-file-text",
        },
        TYPE_LEASE_SIGNED:      {
            "DISPLAY":          "Lease Signed",
            "VERBOSE":          "Lease signed",
            "FA_ICON":          "fa fa-file-text",
        },
        TYPE_MOVING_OUT:          {
            "DISPLAY":          "Moving Out",
            "VERBOSE":          "Move out scheduled in the near future",
            "FA_ICON":          "fa fa-truck",
        },
        TYPE_MOVING_IN:          {
            "DISPLAY":          "Moving In",
            "VERBOSE":          "Move in scheduled in the near future",
            "FA_ICON":          "fa fa-truck",
        },
        TYPE_SERVICE_REQUEST:     {
            "DISPLAY":          "Service Request",
            "VERBOSE":          "Service requested",
            "FA_ICON":          "fa fa-envelope",
        },
        TYPE_WORK_ORDER:              {
            "DISPLAY":          "Work Order",
            "VERBOSE":          "Work order created",
            "FA_ICON":          "fa fa-wrench",
        },
        TYPE_VACANT:              {
            "DISPLAY":          "Vacant",
            "VERBOSE":          "Property currently vacant",
            "FA_ICON":          "fa fa-window-close-o",
        },
        TYPE_TENANTS_NEEDED:      {
            "DISPLAY":          "Tenants Needed",
            "VERBOSE":          "No upcoming tenants planned",
            "FA_ICON":          "fa fa-user-o",
        },
        TYPE_INCIDENT:            {
            "DISPLAY":          "Incident",
            "VERBOSE":          "Incident reported",
            "FA_ICON":          "fa fa-exclamation",
        },
        TYPE_RENT_LATE:           {
            "DISPLAY":          "Rent Paid Late",
            "VERBOSE":          "Rent has not been paid on time",
            "FA_ICON":          "fa fa-clock-o",
        },
        TYPE_EVICTION:            {
            "DISPLAY":          "Eviction",
            "VERBOSE":          "Eviction process has started", 
            "FA_ICON":          "fa fa-sign-out",
        },
        TYPE_OFFICIAL_NOTICE:            {
            "DISPLAY":          "Official Notice",
            "VERBOSE":          "Served official notice", 
            "FA_ICON":          "fa fa-hand-paper-o",
        },
        TYPE_VIOLATION:            {
            "DISPLAY":          "Violation",
            "VERBOSE":          "Violation notice received", 
            "FA_ICON":          "fa fa-hand-paper-o",
        },
        TYPE_TENANT:              {
            "DISPLAY":          "Tenant Issue",
            "VERBOSE":          "Tenant specific issue raised",  
            "FA_ICON":          "fa fa-user-circle-o",
        },
        TYPE_OWNER:               {
            "DISPLAY":          "Owner Issue",
            "VERBOSE":          "Owner specific issue raised",
            "FA_ICON":          "fa fa-user-circle",
        },
        TYPE_INFO_INCOMPLETE:     {
            "DISPLAY":          "Info Incomplete",
            "VERBOSE":          "Information is missing for this record",
            "FA_ICON":          "fa fa-info",
        },
        TYPE_INFO:            {
            "DISPLAY":          "Information",
            "VERBOSE":          "Information reported",
            "FA_ICON":          "fa fa-info",
        },
        TYPE_RENT_PAID:           {
            "DISPLAY":          "Rent Paid",
            "VERBOSE":          "Rent was paid",
            "FA_ICON":          "fa fa-money",
        },
        TYPE_INSPECTION:          {
            "DISPLAY":          "Inspection",
            "VERBOSE":          "Inspection performed on site",
            "FA_ICON":          "fa fa-binoculars",
        },
        TYPE_SERVICE:             {
            "DISPLAY":          "Service",
            "VERBOSE":          "Service performed on site",
            "FA_ICON":          "fa fa-wrench",
        },
    }


    type = models.CharField(max_length=24, choices=(
        (TYPE_LEASE_EXPIRING,    UI_TYPE[TYPE_LEASE_EXPIRING]['DISPLAY']),   
        (TYPE_LEASE_SIGNED,      UI_TYPE[TYPE_LEASE_SIGNED]['DISPLAY']),   
        (TYPE_MOVING_OUT,        UI_TYPE[TYPE_MOVING_OUT]['DISPLAY']),         
        (TYPE_MOVING_IN,         UI_TYPE[TYPE_MOVING_OUT]['DISPLAY']),         
        (TYPE_VACANT,            UI_TYPE[TYPE_VACANT]['DISPLAY']),
        (TYPE_TENANTS_NEEDED,    UI_TYPE[TYPE_TENANTS_NEEDED]['DISPLAY']),
        (TYPE_WORK_ORDER,        UI_TYPE[TYPE_WORK_ORDER]['DISPLAY']),
        (TYPE_SERVICE_REQUEST,   UI_TYPE[TYPE_SERVICE_REQUEST]['DISPLAY']),
        (TYPE_INCIDENT,          UI_TYPE[TYPE_INCIDENT]['DISPLAY']),
        (TYPE_RENT_LATE,         UI_TYPE[TYPE_RENT_LATE]['DISPLAY']),
        (TYPE_EVICTION,          UI_TYPE[TYPE_EVICTION]['DISPLAY']), 
        (TYPE_OFFICIAL_NOTICE,   UI_TYPE[TYPE_OFFICIAL_NOTICE]['DISPLAY']), 
        (TYPE_VIOLATION,         UI_TYPE[TYPE_VIOLATION]['DISPLAY']), 
        (TYPE_TENANT,            UI_TYPE[TYPE_TENANT]['DISPLAY']),
        (TYPE_OWNER,             UI_TYPE[TYPE_OWNER]['DISPLAY']), 
        (TYPE_INFO_INCOMPLETE,   UI_TYPE[TYPE_INFO_INCOMPLETE]['DISPLAY']),    
        (TYPE_INFO,              UI_TYPE[TYPE_INFO]['DISPLAY']),    
        (TYPE_RENT_PAID,         UI_TYPE[TYPE_RENT_PAID]['DISPLAY']),    
        (TYPE_INSPECTION,        UI_TYPE[TYPE_INSPECTION]['DISPLAY']),    
        (TYPE_SERVICE,           UI_TYPE[TYPE_SERVICE]['DISPLAY']),    
    ))

    def type_icon(self):
        return self.UI_TYPE[self.type]['FA_ICON']

    def type_verbose(self):
        return self.UI_TYPE[self.type]['VERBOSE']
    
    def priority_style(self):
        return self.UI_PRIORITY[self.priority]['STYLE']

    def priority_icon(self):
        return self.UI_PRIORITY[self.priority]['FA_ICON']
   

    def isFuture(self):
        return self.activity_on > timezone.now()

    def __str__(self):
        return self.prop.__str__() +' - '+ self.get_type_display() +' - '+ self.get_priority_display() +' - '+ self.activity_on.strftime('%m/%d/%Y')

    def Meta(self):
        verbose_name_plural = 'Property Activities'
        ordering = ["-activity_on"]
        get_latest_by = ["activity_on"]
        
