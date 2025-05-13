from django.contrib import admin
from django.utils.html import format_html

from .models import *


from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle



def export_to_pdf(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 8),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ('user_id', 'property', 'total_price', 'start_date', 'end_date','status')

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.user_id.firstname, obj.property, obj.total_price,obj.start_date,obj.end_date,obj.status])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to PDF"

# Register your models here.

class showregister(admin.ModelAdmin):
    list_display = ["firstname","lastname","email","password","confirmpassword"]

admin.site.register(reigstermodel,showregister)


class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'user','title','description','listing_type','built_up_area','carpet_area','price', 'monthly_rent','construction_status','security_deposit',
        'category', 'bhk_type', 'furnishing_status', 'address', 'city', 'state',
        'pincode','googlemap','video_url', 'virtual_tour', 'age_of_property',
        'facing_direction', 'bedrooms', 'bathrooms', 'balconies', 'floors_no',
        'available_from', 'basement', 'owner_notes','image',
    )

    # def Property_photo(self, obj):
    #     if obj.image:
    #         return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
    #     return "No Image"
    #
    # Property_photo.allow_tags = True

admin.site.register(Property, PropertyAdmin)


class AuctionAdmin(admin.ModelAdmin):
    list_display = ('description','token_amount','category','state', 'city', 'area', 'square_feet','Auction_photo','bhk_type','bank_name', 'reserve_price','EMD', 'start_datetime', 'end_datetime', 'created_at')

    def Auction_photo(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return "No Image"

admin.site.register(Auction,AuctionAdmin)


@admin.register(PlanOrder)
class PlanorderAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'razorpay_order_id', 'razorpay_payment_id', 'razorpay_signature','amount','status','purchase_date','expiration_date')


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'email', 'message', 'contact_number','created_at')


@admin.register(RentingPayment)
class RentingAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'property', 'total_price', 'start_date', 'end_date','razorpay_order_id','status')
    list_filter = ["start_date"]
    actions = [export_to_pdf]

class AuctionTokensAdmin(admin.ModelAdmin):
    list_display = ('userid', 'propertyid', 'price', 'timestamp')


admin.site.register(auctiontokens, AuctionTokensAdmin)

class contactdisplay(admin.ModelAdmin):
    list_display = ('name','email','contactno','subject','message')

admin.site.register(contactmodel,contactdisplay)

class showfeedback(admin.ModelAdmin):
    list_display = ["rating","comment","userid"]

admin.site.register(feedback,showfeedback)