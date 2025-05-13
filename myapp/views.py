from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def aboutpage(request):
    return render(request,"about.html")

def contactpage(request):
    return render(request,"contact.html")
def loginpage(request):
    return render(request,"login.html")


def shop(request):
    fetchauction = Auction.objects.all()
    context = {

        "auction": fetchauction,

    }
    return render(request,"shop.html",context)

def shoplistpage(request):
    fetchauction = Auction.objects.all()
    print(fetchauction)
    context = {
        "data":fetchauction
    }
    return render(request,"shop-list.html",context)


def registerpage(request):
    return render(request,"register.html")

def indexpage(request):
    return render(request,"index.html")

def index6page(request):
    uid = request.session.get('log_id')  # Use .get() to avoid KeyError

    fetchproperty = Property.objects.filter(status=True)
    fetchauction = Auction.objects.all()
    fetchfeedback = feedback.objects.all()

    paid_order = PlanOrder.objects.filter(user_id=uid, status="Paid").order_by("-purchase_date").first()

    context = {
        "property": fetchproperty,
        "auction": fetchauction,
        "paid_order": paid_order,
        "feedback":fetchfeedback,

    }
    return render(request, "index-6.html", context)


def index3page(request):

    return render(request,"index-3.html")

def insertintocart(request):
    userid = request.session["log_id"]
    pid = request.POST.get("pid")
    price = request.POST.get("price")
    title = request.POST.get("title")

    insertquery = cart(userid=reigstermodel(id=userid), propertyid=Auction(id=pid),title=title,
                        price=price, orderid=0, orderstatus=1)
    insertquery.save()
    messages.success(request, "product added to cart")
    return redirect("/")



def cartpage(request):
    userid_loggedin = request.session["log_id"]
    fetchdata = cart.objects.filter(userid=userid_loggedin, orderstatus=1)
    context = {
        "data": fetchdata
    }
    return render(request, "cart.html", context)



def accountpage(request):

    userid_loggedin = request.session["log_id"]

    fetchdata = Property.objects.filter(user=userid_loggedin)
    context = {
        "data": fetchdata
    }

    return render(request,"account.html",context)

def deleteitem(request,id):
    print(id)
    # delete from cart where id=id
    Property.objects.get(id=id).delete()
    messages.success(request,"Item Removed")
    return redirect("/")

def addlistingpage(request):
    return render(request,"add-listing.html")



def productdetailspage(request,id):

    print(id)
    fetchdata = Property.objects.get(id=id)

    context = {
        "data":fetchdata
    }

    return render(request,"product-details.html",context)




def fetchregister(request):

    ufirstname= request.POST.get("firstname")
    ulastname= request.POST.get("lastname")
    uemail= request.POST.get("email")
    upassword= request.POST.get("password")
    uconfirpassword = request.POST.get("confirmpassword")

    insertquery = reigstermodel( firstname=ufirstname, lastname=ulastname, email=uemail, password=upassword, confirmpassword=uconfirpassword )
    insertquery.save()

    return render(request,"login.html")

def fetchlogindata(request):

    useremail = request.POST.get("email")
    userpassword = request.POST.get("password")

    print(useremail)
    print(userpassword)


    try:

        userdata = reigstermodel.objects.get(email=useremail,password=userpassword)
        print("success")
        print(userdata)

        request.session["log_id"] = userdata.id
        request.session["log_firstname"] = userdata.firstname
        request.session["log_lastname"] = userdata.lastname
        request.session["log_email"] = userdata.email


        print("session name", request.session["log_firstname"], request.session["log_lastname"])

    except:

        print("failure")
        userdata = None

    if userdata is not None:
        return redirect("/")
    else:
        print("Invalid email or password")
        messages.error(request, "invalid email or password")

    return render(request,"login.html")

def logout(request):
    try:
        del request.session["log_id"]
        del request.session["log_firstname"]
        del request.session["log_lastname"]
        del request.session["log_email"]
    except:
        pass

    return redirect("/")


def fetchaddproperty(request):
        title = request.POST.get('ltn__name')
        description = request.POST.get('ltn__message')
        listing_type = request.POST.get('listtype')
        built_up_area = request.POST.get('built_up_area')
        if built_up_area:
            built_up_area = built_up_area.replace(',', '')  # Remove commas
            built_up_area = ''.join(filter(str.isdigit, built_up_area))  # Keep only numbers

            try:
                built_up_area = float(built_up_area)  # Convert to a number
            except ValueError:
                built_up_area = None  # Handle invalid input

        carpet_area = request.POST.get('carpet_area')
        if carpet_area:
            carpet_area = carpet_area.replace(',', '')
            carpet_area = ''.join(filter(str.isdigit, carpet_area))

            try:
                carpet_area = float(carpet_area)
            except ValueError:
                carpet_area = None
        if carpet_area == '':

            carpet_area = None  # Convert empty string to None

        price = request.POST.get('price')
        if price:
            price = price.replace(',', '')  # Remove commas
            try:
                price = float(price)  # Convert to a number
            except ValueError:
                price = None  # Handle invalid input

        construction_status = request.POST.get('con_sta')
        monthly_rent = request.POST.get('rent_p')
        if monthly_rent:
            monthly_rent = monthly_rent.replace(',', '')  # Remove commas
            try:
                monthly_rent = float(monthly_rent)  # Convert to a number
            except ValueError:
                monthly_rent = None  # Handle invalid input

        security_deposit = request.POST.get('deposit')
        category = request.POST.get('sel_c')
        bhk_type = request.POST.get('bhk')
        furnishing_status = request.POST.get('furnishing_status')


        address = request.POST.get('address')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        Google_Map_Embed = request.POST.get('Google_Map_Embed')

        match = re.search(r'src="([^"]+)"', Google_Map_Embed)
        googlemap = match.group(1) if match else None


        image = request.FILES["image"]
        #pdf_file = request.FILES.get('pdf_file')
        video_url = request.POST.get('video_url', '').strip()
        virtual_tour = request.POST.get('virtual_tour', '').strip()
        age_of_property = request.POST.get('age_of_property')
        facing_direction = request.POST.get('facing_direction')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        balconies = request.POST.get('balconies')
        floors_no = request.POST.get('floors_no')
        available_from = request.POST.get('available_from')
        basement = request.POST.get('basement')
        owner_notes = request.POST.get('owner_notes')
        userid = request.session["log_id"]

        # Data Insert Query
        insertquery = Property.objects.create(
            user = reigstermodel(id=userid),
            title=title,
            description=description,
            listing_type=listing_type,
            built_up_area=built_up_area,
            carpet_area=carpet_area,
            price=price if price else None,
            construction_status=construction_status,
            monthly_rent=monthly_rent if monthly_rent else None,
            security_deposit=security_deposit,
            category=category,
            bhk_type=bhk_type,
            furnishing_status=furnishing_status,

            address=address,
            country=country,
            state=state,
            city=city,
            pincode=pincode,
            googlemap=googlemap,

            image=image,
            video_url=video_url if video_url else None,
            virtual_tour=virtual_tour if virtual_tour else None,

            age_of_property=age_of_property,
            facing_direction=facing_direction,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            balconies=balconies,
            floors_no=floors_no,
            available_from=available_from,
            basement=basement,
            owner_notes=owner_notes


        )
        insertquery.save()
        messages.success(request, "product added successfully!!")


        return redirect("/")


def property_search(request):
    listing_type = request.POST.get('listing_type')
    property_type = request.POST.get('sel_c')
    city = request.POST.get('location')
    BHK = request.POST.get('BHK')
    #price = request.GET.get('price')

    print(property_type)
    print(city)
    print(BHK)
   # print(price)
    print(listing_type)


    properties = Property.objects.filter(
        Q(category=property_type) |
        Q(city=city) |
        Q(bhk_type=BHK) |
        # Q(price=price) |
        Q(listing_type=listing_type)

    )


    return render(request, "shop-grid.html", {"property": properties})


def allproperty(request):
    uid = request.session['log_id']
    allproperties = Property.objects.filter(user=uid)
    context = {
        'property':allproperties,
    }
    return render(request,'shop-grid.html', context)




def rentproperty(request):
    allproperties = Property.objects.filter(listing_type="Rent",status=True)
    context = {
        'property': allproperties,
    }
    return render(request,"shop-grid.html",context)


def propertyforsale(request):
    allproperties = Property.objects.filter(listing_type="Sale",status=True)
    context = {
        'property': allproperties,
    }
    return render(request,"shop-grid.html",context)


def pricing(request):
    user_id = request.session['log_id']
    user = reigstermodel.objects.get(id=user_id)

    # Fetch all active plans (with Paid status)
    active_plan_orders = PlanOrder.objects.filter(user=user, status='Paid')
    active_plan_ids = active_plan_orders.values_list('plan_id', flat=True)

    # Fetch all available plans
    plans = SubscriptionPlan.objects.all()

    context = {
        'plans': plans,
        'active_plan_ids': list(active_plan_ids),  # Convert to list if necessary
    }

    return render(request,'subscriptionplan.html', context)

import razorpay
from django.conf import settings
from django.shortcuts import render, redirect
from .models import SubscriptionPlan

def create_order(request, plan_id):
    uid = request.session['log_id']
    amount = request.POST.get("price")
    pid = request.POST.get("pid")
    print(amount)
    razorpay_client = razorpay.Client(auth=('rzp_test_VQhEfe2NCXbbwI', '2ibreCYL78DA3kjOhobCvz0f'))

    try:
        fetchdata = auctiontokens.objects.get(userid=uid,propertyid=pid)
        print(fetchdata)
    except:
        fetchdata = None
        print(fetchdata)


    if fetchdata is None:
        storedata = auctiontokens(
            userid = reigstermodel(id=uid),
            propertyid=Auction(id=pid),
            price=amount
        )
        storedata.save()
    else:
        messages.error(request,"You have already applied for auction for this property")
        return redirect("/")




    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create({
        "amount": int(float(amount) * 100),  # Amount in paisa
        "currency": "INR",
        "payment_capture": '1',  # Auto-capture payment after successful
        "receipt": f"order_{uid}",
    })

    context = {
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key_id': 'rzp_test_VQhEfe2NCXbbwI',
        'amount': amount,
        'currency': 'INR',
        'plan': amount,
    }

    return render(request, 'paymentb.html', context)


from django.core.mail import send_mail
from django.shortcuts import render, redirect
import razorpay

def payment_success(request):

    return redirect("/")



def add_renting(request, renting_id):

    """
    View to handle donation form submission and Razorpay payment.
    """
    context = {}

    # Fetch campaign details
    uid = request.session['log_id']
    try:
        campaign_obj = Property.objects.get(id=renting_id)
        campaign_obj.status = False
        campaign_obj.save()
    except Property.DoesNotExist:
        messages.error(request, "Campaign not found!")
        return redirect("campaign_list")  # Redirect to campaign list page
    donor = reigstermodel.objects.get(id=uid)  # Assuming `user` is a ForeignKey in `registermodel`

    if request.method == "POST":
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")


        # Validate the input fields
        if not all([start_date, end_date]):
            messages.error(request, "All fields are required.")
            return redirect('/')

        # Convert total price to integer for Razorpay (in paisa)
        total_price = int(float(campaign_obj.monthly_rent) * 100)

        # Initialize Razorpay client
        razorpay_client = razorpay.Client(auth=('rzp_test_VQhEfe2NCXbbwI', '2ibreCYL78DA3kjOhobCvz0f'))

        # Create Razorpay Order
        try:
            razorpay_order = razorpay_client.order.create({
                "amount": total_price,  # Amount in paisa
                "currency": "INR",
                "payment_capture": '1',  # Auto-capture payment
                "receipt": f"order_{renting_id}_{timezone.now().timestamp()}",
            })
        except Exception as e:
            messages.error(request, f"Payment error: {str(e)}")
            return redirect('/')

        # Create a new donation record in DB
        donation_obj = RentingPayment.objects.create(
            user_id=donor,  # Use registermodel instance
            property=campaign_obj,
            total_price=total_price / 100,  # Convert back to decimal
            start_date=start_date,
            end_date=end_date,
            razorpay_order_id=razorpay_order["id"],
            status="Pending",
        )




        # Pass Razorpay details to template
        context.update({
            "razorpay_order_id": razorpay_order["id"],
            "amount": total_price / 100,
            "currency": "INR",
            "campaign": campaign_obj,
            "donation": donation_obj,
            'razorpay_key_id': 'rzp_test_VQhEfe2NCXbbwI',
        })

        return render(request, "payment.html", context)

    return render(request, "add_renting_detail.html", {"campaign": campaign_obj})

from django.core.mail import send_mail


import razorpay
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import RentingPayment

RAZORPAY_KEY_ID ='rzp_test_VQhEfe2NCXbbwI'
RAZORPAY_SECRET_KEY ='2ibreCYL78DA3kjOhobCvz0f'

@csrf_exempt
def verify_payment(request, donation_id):
    if request.method == "POST":
        razorpay_payment_id = request.POST.get("razorpay_payment_id")
        razorpay_order_id = request.POST.get("razorpay_order_id")
        razorpay_signature = request.POST.get("razorpay_signature")

        print("Razorpay Payment ID:", razorpay_payment_id)
        print("Razorpay Order ID:", razorpay_order_id)
        print("Razorpay Signature:", razorpay_signature)  # Check if it's None

        if not razorpay_signature:
            messages.error(request, "Payment verification failed: Signature missing!")
            return redirect("donation_form")

        donation_obj = RentingPayment.objects.get(id=donation_id)

        client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET_KEY))

        # Verify payment signature
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            donation_obj.status = "Paid"
            donation_obj.razorpay_payment_id = razorpay_payment_id
            donation_obj.save()
            messages.success(request, "Payment successful! Thank you for your support.")
        except Exception as e:
            print("Payment Verification Error:", e)
            donation_obj.status = "Failed"
            donation_obj.save()
            messages.error(request, "Payment verification failed!")

        return render(request, 'success.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Inquiry

def inquiry_form(request, property_id):
    uid = request.session['log_id']
    property_obj = get_object_or_404(Property, id=property_id)
    try:
        fetchdata = Inquiry.objects.get(user__id=uid, property__id=property_id)
        print(fetchdata)
    except Exception as e:
        fetchdata = None
        print(e)
    if fetchdata is None:
        if request.method == "POST":
            email = request.POST.get("email")
            contact_number = request.POST.get("contact_number")
            message = request.POST.get("message")
            # Ensure the user is logged in before saving the inquiry

            if request.user.is_authenticated:
                Inquiry.objects.create(
                    user=reigstermodel(id=uid),
                    property=property_obj,  # Link property
                    email=email,
                    contact_number=contact_number,
                    message=message,
                )
                return redirect("/")  # Redirect to success page
    else:
        messages.error(request, "You have already applied for inquiry for this property")
        return redirect("/")

    return render(request, "inquiry_form.html", {"property": property_obj})



def forgotpage(request):
    return render(request,"forgotpass.html")

def forgotpassword(request, registermodel=None):
    if request.method == 'POST':
        username = request.POST['email']
        try:
            user = reigstermodel.objects.get(email=username)

        except reigstermodel.DoesNotExist:
            user = None
        #if user exist then only below condition will run otherwise it will give error as described in else condition.
        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################


            msg = "hello here it is your new password  "+password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'krushanuinfolabz@gmail.com',
                [username],
                fail_silently=False,
            )

            #now update the password in model
            cuser = reigstermodel.objects.get(email=username)
            cuser.password = password
            cuser.save(update_fields=['password'])

            print('Mail sent')
            messages.info(request, 'mail is sent')
            return redirect("/")

        else:
            messages.info(request, 'This account does not exist')
    return redirect("/")



def updatepass(request):
    userid = request.session["log_id"]
    npass = request.POST.get("npass")
    opass = request.POST.get("opass")
    cpass = request.POST.get("cpass")

    fetchdata = reigstermodel.objects.get(id=userid)
    originalpass = fetchdata.password

    if opass==originalpass:
        if npass==cpass:
            fetchdata.password = npass
            fetchdata.save()
            return redirect("/")
        else:
            messages.error(request,"password and confirm pass should be same")
    else:
        messages.error(request,"Wrong Old Password")

    return render(request, "account.html")

def myrentprop(request):
    userid = request.session["log_id"]
    fetchdata = RentingPayment.objects.filter(user_id=userid)
    print(fetchdata)
    context = {
        "data":fetchdata
    }
    return render(request,"myproperty.html",context)

def myrent(request):
    userid = request.session["log_id"]
    propertydata = Property.objects.filter(user_id=userid)
    fetchdata = RentingPayment.objects.filter(property__in=propertydata)
    print(fetchdata)
    context = {
        "data":fetchdata
    }
    return render(request,"renthistory.html",context)

def myauctprop(request):
    userid = request.session["log_id"]
    fetchdata = auctiontokens.objects.filter(userid=userid)
    print(fetchdata)
    context = {
        "data":fetchdata
    }
    return render(request,"myauctionprop.html",context)

def myinquiry(request):
    userid = request.session["log_id"]
    fetchdata = Inquiry.objects.filter(user_id=userid)
    print(fetchdata)
    context = {
        "data": fetchdata
    }
    return render(request,"myinquiry.html",context)

def fetchcontact(request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        contactno = request.POST.get('contactno')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        insertquery = contactmodel(name=name,email=email,contactno=contactno,subject=subject,message=message)
        insertquery.save()


        messages.success(request, "message send successfully!!")

        return render(request,"contact.html")

def feedbackpage(request):
    return render(request,"feedback.html")


def fetchfeedback(request):
    urating = request.POST.get("rating")
    ucomment = request.POST.get("message")

    userid = request.session["log_id"]

    insertquery = feedback(rating=urating,comment=ucomment, userid=reigstermodel(id=userid))
    insertquery.save()

    messages.success(request, "reply feedback successfully!!")
    return render(request, "feedback.html")