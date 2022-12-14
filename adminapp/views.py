from django.shortcuts import redirect, render
from django.contrib import messages
from adminapp.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from mechanicapp.models import Mechanic_detailsModel
from userapp.models import FeedbackModel, UserBookingModel, UserDetailsModel
# Create your views here.

def admin_login(request):
    print('get')
    if request.method == "POST":
        print('post')
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email == "admin" and password == "admin" :
            messages.info(request, "Login Successfully.")
            return redirect("admin_dashboard")
            
        else:
            messages.error(request,"Invalid EmailID or Password")
            return redirect("admin_login")
    return render(request,'main/admin-login.html')

def admin_logout(request):
    return redirect('index')

def admin_dashboard(request):
    a = UserDetailsModel.objects.all().count()
    b = Mechanic_detailsModel.objects.all().count()
    c = UserBookingModel.objects.filter(status='Pending').count()
    d = Mechanic_detailsModel.objects.filter(status='UnAuthorized').count()
    return render(request,'admin/admin-dashboard.html',{'a':a,'b':b,'c':c,'d':d})

def admin_add_authority(request):
    if request.method == "POST":
        authorityname = request.POST['name']
        contact_number = request.POST['mobileno']
        city = request.POST['city']
        AuthorityModel.objects.create(authority_name=authorityname, contact_number=contact_number, city=city)
        messages.info(request, 'Authority Add Succssfully')
        return redirect('admin_add_authority')
    else:
        return render(request,'admin/admin-add-authority.html')

def admin_manage_authority(request):
    a = AuthorityModel.objects.all()
    return render(request,'admin/admin-manage-authority.html',{'a':a})

def admin_edit_authority(request,id):
    b = AuthorityModel.objects.get(authority_id=id)
    data = get_object_or_404(AuthorityModel, authority_id=id)
    if request.method == "POST":
        authorityname = request.POST['name']
        contact_number = request.POST['mobileno']
        city = request.POST['city']

        data.authority_name = authorityname
        data.contact_number = contact_number
        data.city = city
        data.save(update_fields=['authority_name', 'contact_number','city'])
        data.save()
        messages.info(request, 'Authority Updated Succssfully')
        return redirect(admin_dashboard)
    else:
        return render(request,'admin/admin-edit-authority.html',{'b':b})

def admin_manage_mechanic(request):
    status = Mechanic_detailsModel.objects.exclude(status='Pending')
    return render(request,'admin/admin-manage-mechanic.html',{'status':status})

def admin_pending_mechanic(request):
    mechanic = Mechanic_detailsModel.objects.filter(status='Pending')
    return render(request,'admin/admin-pending-mechanic.html',{'mechanic':mechanic})

def admin_all_mechanic(request):
    all = Mechanic_detailsModel.objects.all()
    return render(request,'admin/admin-all-mechanic.html',{'all':all})

def manage(request,id):
    data = get_object_or_404(Mechanic_detailsModel,mechanic_id=id)
    if data.status == 'Authorized':
        data.status='UnAuthorized'
        data.save(update_fields=['status'])
        data.save()
        return redirect('admin_dashboard')
    else:
        data.status='Authorized'
        data.save(update_fields=['status'])
        data.save()
        return redirect('admin_dashboard')

def update(request,id):
    data = get_object_or_404(Mechanic_detailsModel,mechanic_id=id)
    data.status='Authorized'
    data.save(update_fields=['status'])
    data.save()
    # messages.info(request,"Checked Successfully")
    return redirect('admin_dashboard')

def reject(request,id):
    data = get_object_or_404(Mechanic_detailsModel,mechanic_id=id)
    data.status='UnAuthorized'
    data.save(update_fields=['status'])
    data.save()
    # messages.info(request,"Checked Successfully")
    return redirect('admin_dashboard')

def admin_user_details(request):
    details = UserDetailsModel.objects.all()
    if request.method == 'POST'  :
        print('hi')
        search = request.POST.get('search')
        print(search)
        # print('jj')
        details = UserDetailsModel.objects.filter(Q(user_name__contains=search)|Q(user_email__contains=search)|Q(user_number__contains=search)|Q(user_city__contains=search))
        print(details)
        # c = UserBookingModel.objects.filter()
        # p = Paginator(c,)
        # page_number = request.GET.get('page')
        # ServiceDatafinal=p.get_page(page_number)
        return render(request, 'admin/admin-user-details.html',{'user':details})
    else:
        return render(request,'admin/admin-user-details.html',{'user':details})

def admin_feedback_analysis(request):
    feedback = FeedbackModel.objects.all()
    return render(request,'admin/admin-feedback-analysis.html',{'feedback':feedback})

def admin_sentement_analysis_graph(request):
    vpositive= FeedbackModel.objects.filter(sentiment='Very Positive').count()
    vnegitive = FeedbackModel.objects.filter(sentiment='Very Negitive').count()
    positive = FeedbackModel.objects.filter(sentiment='Positive').count()
    negitive = FeedbackModel.objects.filter(sentiment='Negitive').count()
    neutral = FeedbackModel.objects.filter(sentiment='Neutral').count()
    return render(request,'admin/admin-sentement-analysis-graph.html',{'vpositive':vpositive,'vnegitive':vnegitive,'positive':positive,'negitive':negitive,'neutral':neutral})


