import re
from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.utils.timezone import now

# Create your models here.

class reigstermodel(models.Model):
    firstname= models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    confirmpassword = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname

from django.db import models

class Property(models.Model):
    user = models.ForeignKey(reigstermodel, on_delete=models.CASCADE, null=True, blank=True, related_name='user_property')
    title = models.CharField(max_length=255)
    description = models.TextField()
    listing_type = models.CharField(max_length=50, choices=[('Rent', 'Rent'), ('Sale', 'Sale')],null=True)
    built_up_area = models.FloatField(null=True, blank=True)
    carpet_area = models.FloatField(null=True,blank=True)
    price = models.FloatField(null=True, blank=True)#models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    construction_status = models.CharField(max_length=50, choices=[('Ready to Move', 'Ready to Move'), ('Under construction', 'Under construction')])
    monthly_rent = models.FloatField(null=True, blank=True)#models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    security_deposit = models.CharField(max_length=50, choices=[('None', 'None'), ('1 month', '1 month'), ('2 month', '2 month'), ('Custom', 'Custom')],null=True, blank=True)
    category = models.CharField(max_length=50, choices=[('Apartments', 'Apartments'), ('Duplexes', 'Duplexes'), ('Houses', 'Houses'), ('Villas', 'Villas')])
    bhk_type = models.CharField(max_length=50, choices=[('1 RK', '1 RK'), ('1 BHK', '1 BHK'), ('1.5 BHK', '1.5 BHK'), ('2 BHK', '2 BHK'), ('3+ BHK', '3+ BHK')])
    furnishing_status = models.CharField(max_length=50, choices=[('Furnished', 'Furnished'), ('Semi-Furnished', 'Semi-Furnished'), ('Unfurnished', 'Unfurnished')])

    def __str__(self):
        return self.title

    address = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    googlemap = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to='photos',null=True, blank=True)

    video_url = models.TextField(null=True, blank=True)
    virtual_tour = models.TextField(null=True, blank=True)

    def Property_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))

    Property_photo.allow_tags = True
    status = models.BooleanField(default=True)

    # def Property_photo2(self):
    #     return mark_safe('<img src="{}" width="100"/>'.format(self.pdf_file.url))
    #
    # Property_photo2.allow_tags = True





    age_of_property = models.CharField(max_length=50, blank=True, null=True)
    facing_direction = models.CharField(
        max_length=10,
        choices=[("North", "North"), ("East", "East"), ("West", "West"), ("South", "South")],
        blank=True,
        null=True
    )
    bedrooms = models.PositiveIntegerField(blank=True, null=True)
    bathrooms = models.PositiveIntegerField(blank=True, null=True)
    balconies = models.PositiveIntegerField(blank=True, null=True)
    floors_no = models.CharField(max_length=20, blank=True, null=True)
    available_from = models.DateField(blank=True, null=True)
    basement = models.CharField(max_length=255, blank=True, null=True)
    owner_notes = models.TextField(blank=True, null=True)



class Auction(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('villa', 'Villa'),
        ('land', 'Land'),
        ('commercial', 'Commercial Property'),
    ]

    category = models.CharField(max_length=50, choices=[('Apartments', 'Apartments'), ('Duplexes', 'Duplexes'), ('Houses', 'Houses'), ('Villas', 'Villas')], null=True, blank=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=255)  # Specific locality
    square_feet = models.PositiveIntegerField()
    image = models.ImageField(upload_to='photos',null=True, blank=True)
    bhk_type = models.CharField(max_length=50, choices=[('1 RK', '1 RK'), ('1 BHK', '1 BHK'), ('1.5 BHK', '1.5 BHK'),('2 BHK', '2 BHK'), ('3+ BHK', '3+ BHK')], null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    reserve_price = models.DecimalField(max_digits=12, decimal_places=2)  # Minimum starting price
    EMD = models.DecimalField(max_digits=12, decimal_places=2)  # Earnest Money Deposit
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    token_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def Auction_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))

    Auction_photo.allow_tags = True



class cart(models.Model):

    userid = models.ForeignKey(reigstermodel,on_delete=models.CASCADE)
    propertyid = models.ForeignKey(Auction,on_delete=models.CASCADE)
    price = models.FloatField()
    title = models.CharField(max_length=100)
    orderstatus = models.IntegerField()  # 1 - added , 0 - orederplace/remove
    orderid = models.IntegerField()  # default - 0 , update orderid when user placed the order

from django.utils import timezone
from dateutil.relativedelta import relativedelta  # Use this for month-based delta
class SubscriptionPlan(models.Model):
    plan_name = models.CharField(max_length=255, null=False)  # Name of the subscription
    plan_duration = models.IntegerField(null=False)  # Duration in days or months
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)  # Price of the subscription plan
    description = models.TextField(blank=True, null=True)  # Description of the plan
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Discount percentage, if applicable
    renewable = models.BooleanField(default=True)  # Whether the plan is renewable
    max_properties = models.IntegerField(default=1)  # Max properties allowed to list under this plan
    creation_date = models.DateTimeField(auto_now_add=True)  # Creation date
    def __str__(self):
        return f"{self.plan_name} ({self.plan_duration} days) - ${self.price}"

class PlanOrder(models.Model):
    user = models.ForeignKey(reigstermodel, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Failed', 'Failed')], default='Pending')
    purchase_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Ensure purchase_date is set before calculating expiration_date
        if not self.expiration_date and self.purchase_date:
            self.expiration_date = self.purchase_date + relativedelta(months=self.plan.plan_duration)
        super().save(*args, **kwargs)

    def is_active(self):
        # Check if the current date is before the expiration date
        return self.expiration_date and self.expiration_date > timezone.now()

    def has_personal_trainer(self):
        # Check if the associated plan includes a personal trainer
        return self.plan.personal_trainer if hasattr(self.plan, 'personal_trainer') else False

    def __str__(self):
        return f"Order {self.razorpay_order_id} by {self.user}"

from django.db import models
from django.contrib.auth.models import User  # Assuming you're using Django's built-in User model

class Inquiry(models.Model):
    user = models.ForeignKey(reigstermodel, on_delete=models.CASCADE)  # User who is making the inquiry
    property = models.ForeignKey(Property, on_delete=models.CASCADE)  # Property being inquired about
    email = models.EmailField()  # User's email
    message = models.TextField()  # Inquiry details
    contact_number = models.CharField(max_length=15)  # User's contact number
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"Inquiry by {self.user.firstname}"


class RentingPayment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid'),
    ]
    user_id=models.ForeignKey(reigstermodel,on_delete=models.CASCADE, default='')
    property=models.ForeignKey(Property,on_delete=models.CASCADE,null=True, blank=True)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()  # Rental start date
    end_date = models.DateField()  # Rental end date
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')


class auctiontokens(models.Model):
    userid = models.ForeignKey(reigstermodel,on_delete=models.CASCADE)
    propertyid = models.ForeignKey(Auction, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField()
    timestamp = models.DateField(auto_now=True)

class contactmodel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    contactno=models.BigIntegerField()
    message=models.TextField()

class feedback(models.Model):
    userid = models.ForeignKey(reigstermodel, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()