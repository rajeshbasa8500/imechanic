from django.shortcuts import redirect, render 
from django.shortcuts import get_object_or_404
import mechanicapp
from mechanicapp.models import *
from userapp.models import *
from django.contrib import messages
from django.conf import settings
from django.db.models import Q

from userapp.models import FeedbackModel, UserBookingModel
from userapp.views import user_book_appointment
# Create your views here.
def mechanic_register(request):
    if request.method == "POST" and request.FILES['mphoto']:
        m_name=request.POST['name']
        m_email=request.POST['email']
        m_number=request.POST['number']
        m_city=request.POST['city']
        m_password=request.POST['password']
        m_photo=request.FILES['mphoto']
        try:
            Mechanic_detailsModel.objects.get(mechanic_email=m_email)
            messages.error(request, "Mechanic Email Already Exit.")
            return redirect('mechanic_register')
        except:
            Mechanic_detailsModel.objects.create(mechanic_name=m_name, mechanic_email=m_email, mechanic_number=m_number,
                                             mechanic_city=m_city, mechanic_password=m_password, mechanic_pic=m_photo)
            messages.info(request, "Registration Successfully.")
            return redirect('mechanic_login')
    else:
        return render(request, 'main/mechanic-register.html')

def mechanic_login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password= request.POST["password"] 
        status = 'Authorized'
        try:
            mechanic = Mechanic_detailsModel.objects.get(mechanic_email=email, mechanic_password=password,status=status)
            request.session['mechanic_id'] = mechanic.mechanic_id
            messages.info(request, "Login Successfully.")
            return redirect("mechanic_dashboard")        
        except:
            print('error')
            messages.error(request,"Invalid EmailID or Password")    
    return render(request, 'main/mechanic-login.html')

def mechanic_logout(request):
    return redirect('index')

def mechanic_add_shop(request):
    if request.method=="POST":
        shopname=request.POST["name"]
        print(shopname)
        shopaddress= request.POST["address"]
        shopnumber= request.POST["number"]
        
        Mechanic_shopModel.objects.create(shop_name=shopname, shop_address=shopaddress, contact_number=shopnumber)
        messages.info(request, "Mechanic Shop Add Successfully.")
        return redirect('mechanic_dashboard')
    else:
        return render(request, 'mechanic/mechanic-add-shop.html')

def mechanic_manage_shop(request):
    a = Mechanic_shopModel.objects.all()
    return render(request, 'mechanic/mechanic-manage-shop.html',{'a':a})

def mechanic_edit_shop(request,id):
    b =  Mechanic_shopModel.objects.get(shop_id=id)
    data = get_object_or_404(Mechanic_shopModel, shop_id=id)
    if request.method == "POST":
        shopname=request.POST["name"]
        print(shopname)
        shopaddress= request.POST["address"]
        shopnumber= request.POST["number"]

        data.shop_name = shopname
        data.shop_address = shopaddress
        data.contact_number = shopnumber
        data.save(update_fields=['shop_name', 'shop_address','contact_number'])
        data.save()
        messages.info(request, "Mechanic Shop Updated Successfully.")
        return redirect('mechanic_manage_shop')
    else:
        return render(request, 'mechanic/mechanic-edit-shop.html',{'b':b})

def mechanic_pending_booking(request):
    mechanic_id = request.session['mechanic_id'] 
    c = Mechanic_detailsModel.objects.get(mechanic_id=mechanic_id)
    bookings = UserBookingModel.objects.filter(status='Pending',mechanic=c).order_by('-booking_id')
    booking = UserBookingModel.objects.filter(status='Pending',mechanic=None)
    print(booking,'dddddd')
    return render(request, 'mechanic/mechanic-pending-booking.html',{'bookings':bookings,'booking':booking})

def mechanic_confirmed_booking(request):
    mechanic_id = request.session['mechanic_id'] 
    c = Mechanic_detailsModel.objects.get(mechanic_id=mechanic_id)
    bookings = UserBookingModel.objects.filter(status='Accepted',mechanic=c)
    if request.method == 'POST'  :
        print('hi')
        search = request.POST.get('search')
        print(search)
        # print('jj')
        bookings = UserBookingModel.objects.filter(Q(booking_id__contains=search)|Q(service_type__contains=search)|Q(user__user_name__contains=search)|Q(user__user_number__contains=search)|Q(vehicle_number__contains=search)|Q(booking_date__contains=search))
        print(c)
        # c = UserBookingModel.objects.filter()
        # p = Paginator(c,)
        # page_number = request.GET.get('page')
        # ServiceDatafinal=p.get_page(page_number)
        return render(request, 'mechanic/mechanic-confirmed-booking.html',{'booked':bookings})
    else:
        return render(request, 'mechanic/mechanic-confirmed-booking.html',{'booked':bookings})
    
    

def mechanic_dashboard(request):
    a = UserDetailsModel.objects.all().count()
    b = Mechanic_detailsModel.objects.all().count()
    c = UserBookingModel.objects.filter(status='Pending').count()
    d = Mechanic_detailsModel.objects.filter(status='UnAuthorized').count()
    return render(request, 'mechanic/mechanic-dashboard.html',{'a':a,'b':b,'c':c,'d':d})

def mechanic_my_feedback(request):
    mechanic_id = request.session['mechanic_id']
    mech = Mechanic_detailsModel.objects.get(mechanic_id=mechanic_id)
    a = mech.mechanic_id
    print(a)
    feedback = FeedbackModel.objects.filter(booking__mechanic=a)
    return render(request, 'mechanic/mechanic-my-feedback.html',{'feedback':feedback})

def map(request,id):
    mechanic_id = request.session['mechanic_id']
    c = Mechanic_detailsModel.objects.get(mechanic_id=mechanic_id) 
    print(id)
    a = settings.GOOGLE_API_KEY
    b = UserBookingModel.objects.get(booking_id=id) 
    return render(request, 'mechanic/map.html',{'a':a,'b':b,'c':c})

def accept(request,book_id):
    mechanic_id = request.session['mechanic_id'] 
    order = get_object_or_404(UserBookingModel,booking_id=book_id)
    print(order,'id this is')
    c = Mechanic_detailsModel.objects.get(mechanic_id=mechanic_id)
    mechanic=c
    print(c,'mechanic_id')
    print(order,'hii')
    order.status='Accepted'
    order.mechanic = mechanic
    order.save(update_fields=['status','mechanic'])
    order.save()
    messages.info(request, "Request Accepted Successfully.")
    return redirect('mechanic_dashboard')

# def search(request):
#     print('hi')
#     search = request.GET.get('search')
#     print(search)
#     # print('jj')
#     bookings = UserBookingModel.objects.filter(Q(booking_id__contains=search)|Q(service_type__contains=search)|Q(user__user_name__contains=search)|Q(user__user_number__contains=search)|Q(vehicle_number__contains=search)|Q(customer_name__contains=search)|Q(booking_date__contains=search))
#     return render(request, 'mechanic/mechanic-confirmed-booking.html',{'booked':bookings})  

