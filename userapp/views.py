# from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
# import mechanicapp
from mechanicapp.models import Mechanic_detailsModel
from userapp.models import *
from django.conf import settings
from django.contrib import messages
# import requests
# import json
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from django.db.models import Avg
import googlemaps 
# from .mixins import Directions

# Create your views here.
def user_login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password= request.POST["password"] 
        try: 
            mechanic = UserDetailsModel.objects.get(user_email=email, user_password=password)
            request.session['user_id'] = mechanic.user_id
            messages.info(request, "Login Successfully.")
            return redirect("user_dashboard")        
        except:
            print('error')
            messages.error(request,"Invalid EmailID or Password") 
    return render(request, 'user/user-login.html')

def user_registration(request):
    if request.method == "POST" and request.FILES['uphoto']:
        u_name=request.POST['name']
        u_email=request.POST['email']
        u_number=request.POST['number']
        u_city=request.POST['city']
        u_password=request.POST['password']
        u_photo=request.FILES['uphoto']
        try:
            UserDetailsModel.objects.get(user_email=u_email)
            messages.error(request, "User Email Already Exit.")
            return redirect('user_registration')
        except:
            UserDetailsModel.objects.create(user_name=u_name, user_email=u_email, user_number=u_number,
                                             user_city=u_city, user_password=u_password, user_pic=u_photo)
            messages.info(request, "Registration Successfully.")
            return redirect('user_login')
    else:
        return render(request, 'user/user-registration.html')

def user_dashboard(request):
    a = UserDetailsModel.objects.all().count()
    b = UserBookingModel.objects.all().count()
    return render(request, 'user/user-dashboard.html',{'a':a,'b':b})

def user_book_appointment(request):
    user_id = request.session["user_id"]
    j = UserDetailsModel.objects.get(user_id=user_id)
    print(j)
    a = settings.GOOGLE_API_KEY
    if request.method =="POST":
        service_type = request.POST['servicetype']
        vehicle_type = request.POST['vehicletype']
        vehicle_number = request.POST['vehicleno']
        user_problem = request.POST['problem']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        gmaps = googlemaps.Client(key=a)
        reverse_geocode_result = gmaps.reverse_geocode((latitude,longitude))
        # print(f"reverse_geocode: {reverse_geocode_result[0]['address_components'][1]['long_name']}")
        print(f"reverse_geocode: {reverse_geocode_result[0]['address_components'][1]['long_name']}")
        print(f"reverse_geocode: {reverse_geocode_result[0]['address_components'][2]['long_name']}")
        first = reverse_geocode_result[0]['address_components'][1]['long_name']
        second = reverse_geocode_result[0]['address_components'][2]['long_name']
        full_address = first+ ',' + second
        print(full_address)        
        UserBookingModel.objects.create(service_type=service_type, vehicle_type=vehicle_type, vehicle_number=vehicle_number,
                                        user_problem=user_problem,latitude=latitude,longitude=longitude,user=j,booking_type='Remote Booking',remote_address=full_address)
        messages.info(request, "Booked Successfully.")
        return redirect('user_dashboard') 
    else:
        return render(request, 'user/user-book-appointment.html',{"a":a})

def user_feedback(request,id,mechanic):
    user_id = request.session["user_id"]
    user = UserDetailsModel.objects.get(user_id=user_id)
    book = UserBookingModel.objects.get(booking_id=id)
    mechanic = Mechanic_detailsModel.objects.get(mechanic_id=mechanic)
    print(mechanic,'hi')
    print(user,book,'j')
    if request.method =="POST":
        if not request.POST.get('a'):
            messages.error(request, "Feeback not Sent Please give the star Rating")
            return redirect('user_my_booking')
            
        star = request.POST.get('a')
        comment = request.POST.get('comment')
        # text analysis
        analysis = TextBlob(comment,analyzer=NaiveBayesAnalyzer())
        print(analysis.sentiment)
        
        sentiment = ''
        if analysis.polarity >= 0.5:
            sentiment = 'Very Positive'
        elif analysis.polarity > 0 and analysis.polarity < 0.5:
            sentiment = 'Positive'
        elif analysis.polarity < 0 and analysis.polarity >= -0.5:
            sentiment = 'Negitive'
        elif analysis.polarity <= -0.5:
            sentiment = 'Very Negitive'
        else:
            sentiment = 'Neutral'
            
        FeedbackModel.objects.create(rating=star,comment=comment,sentiment=sentiment,user=user,booking=book,mechanic=mechanic)
        book.feedbackstatus = 'Completed'
        book.save(update_fields=['feedbackstatus'])
        book.save()
        a = FeedbackModel.objects.filter(mechanic=mechanic).aggregate(avarage=Avg('rating'))
        a = a['avarage']
        a=round(a)
        # print(a)
        mechanic.average=a
        mechanic.save(update_fields=['average'])
        mechanic.save()
        messages.info(request, "Feedback Sent Successfully.")
        return redirect('user_dashboard') 
    else:
        return render(request, 'user/user-feedback.html')

def user_book_mechanic(request):
    mechanic= Mechanic_detailsModel.objects.filter(status='Authorized')
    return render(request,'user/user-book-mechanic.html',{'mech':mechanic})

def user_mechanic_appoinement(request,id):
    user_id = request.session["user_id"]
    j = UserDetailsModel.objects.get(user_id=user_id)
    i = Mechanic_detailsModel.objects.get(mechanic_id=id)
    print(j)
    if request.method =="POST":
        service_type = request.POST['servicetype']
        vehicle_type = request.POST['vehicletype']
        vehicle_number = request.POST['vehicleno']
        booking_date =request.POST['date']
        booking_time = request.POST['time']
        user_problem = request.POST['problem']
        
        UserBookingModel.objects.create(service_type=service_type, vehicle_type=vehicle_type, vehicle_number=vehicle_number,
                                        booking_date=booking_date, booking_time=booking_time,
                                        user_problem=user_problem,user=j,mechanic=i,booking_type='Normal Booking')
        messages.info(request, "Booked Successfully.")
        return redirect('user_dashboard') 
    else:
        return render(request, 'user/user-machanic-appoinement.html')

def user_my_booking(request):
    user_id = request.session["user_id"]
    mybooked = UserBookingModel.objects.filter(user=user_id,feedbackstatus='Pending')
    return render(request, 'user/user-my-booking.html',{'mybooked':mybooked})

def user_myprofile(request):
    user_id = request.session["user_id"]
    j = UserDetailsModel.objects.get(user_id=user_id)
    obj = get_object_or_404(UserDetailsModel, user_id=user_id)
    if request.method == 'POST':
        user_name = request.POST['username']
        user_email = request.POST['email']
        user_number = request.POST['number']
        user_city = request.POST['city']
        user_password = request.POST['password']
       
        if not request.FILES.get("uphoto",False):
            # print("yes efffeg jfkdftjhkt")
            obj.user_name = user_name
            obj.user_email = user_email
            obj.user_number = user_number
            obj.user_city = user_city
            obj.user_password = user_password
            obj.save(update_fields=['user_name', 'user_email', 'user_number',
                                        'user_city', 'user_password'])
            obj.save()
             
        elif request.FILES.get("uphoto",False):
            user_pic = request.FILES['uphoto']
            obj.user_name = user_name
            obj.user_email = user_email
            obj.user_number = user_number
            obj.user_city = user_city
            obj.user_password = user_password
            obj.user_pic = user_pic
            obj.save(update_fields=['user_name', 'user_email', 'user_number',
                                        'user_city', 'user_password', 'user_pic'])
            obj.save()
           
           
        messages.info(request, 'Profile Updated Successfully.')       
    return render(request, 'user/user-myprofile.html',{'i':j})

def user_services(request):
    return render(request, 'user/user-services.html')

def user_map(request):
    # a =settings.GOOGLE_API_KEY
    return render(request, 'user/user-map.html')